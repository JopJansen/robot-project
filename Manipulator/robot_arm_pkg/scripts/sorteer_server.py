#! /usr/bin/env python
# -*- coding: utf-8 -*-

# === Importeer ROS en MoveIt bibliotheken ===
import rospy
import sys
import math
import actionlib
import tf2_ros
import tf2_geometry_msgs

import moveit_commander
import moveit_msgs.msg
from geometry_msgs.msg import Pose
from tf.transformations import quaternion_from_euler, quaternion_multiply
from xarm_msgs.srv import SetInt16

# === Importeer de gegenereerde Action types ===
from robot_arm_pkg.msg import SorterenAction, SorterenFeedback, SorterenResult

# === Functie om gripper aan of uit te zetten ===
def control_gripper(state):
    rospy.wait_for_service('/ufactory/vacuum_gripper_set')
    try:
        gripper_service = rospy.ServiceProxy('/ufactory/vacuum_gripper_set', SetInt16)
        gripper_service(bool(state))
    except rospy.ServiceException as e:
        rospy.logerr("Vacuumgripper service call failed: %s", e)

# === Callbackfunctie: wordt aangeroepen als er een action goal binnenkomt ===
def sorteer_callback(goal):
    feedback = SorterenFeedback()
    result = SorterenResult()

    try:
        # === Stap 1: Haal informatie uit goal ===
        tf_frame = goal.tf_frame              # bijv. 'ik_testpoint'
        doel_positie = goal.doel_positie      # bijv. 'bak_rb'

        # === Stap 2: Ga naar 'home' positie ===
        group.go(group.get_named_target_values("home"), wait=True)
        feedback.status = "Naar home gegaan"
        server.publish_feedback(feedback)

        # === Stap 3: Zoek object via TF ===
        transform = tf_buffer.lookup_transform('world', tf_frame, rospy.Time())
        destination_pose = Pose()
        destination_pose.position = transform.transform.translation
        destination_pose.orientation = transform.transform.rotation

        # === Rotatie aanpassen voor juiste gripperoriëntatie ===
        q_orig = [transform.transform.rotation.x,
                  transform.transform.rotation.y,
                  transform.transform.rotation.z,
                  transform.transform.rotation.w]
        q_rot = quaternion_from_euler(math.pi, 0, 0)  # draai 180 graden om X-as
        q_new = quaternion_multiply(q_rot, q_orig)

        destination_pose.orientation.x = q_new[0]
        destination_pose.orientation.y = q_new[1]
        destination_pose.orientation.z = q_new[2]
        destination_pose.orientation.w = q_new[3]

        # === Beweeg naar object ===
        group.set_pose_target(destination_pose)
        group.go(wait=True)
        feedback.status = "Object bereikt"
        server.publish_feedback(feedback)

        # === Beweeg 5 cm omlaag ===
        pose = group.get_current_pose()
        posetarget = pose
        posetarget.pose.position.z -= 0.05
        group.set_pose_target(posetarget)
        group.go(wait=True)

        # === Gripper sluiten ===
        control_gripper(1)
        rospy.sleep(1)
        feedback.status = "Object opgepakt"
        server.publish_feedback(feedback)

        # === Ga naar stand_by ===
        group.go(group.get_named_target_values("stand_by"), wait=True)

        # === Ga naar gewenste sorteerbak ===
        group.set_start_state_to_current_state()
        group.go(group.get_named_target_values(doel_positie), wait=True)
        feedback.status = "Object gesorteerd"
        server.publish_feedback(feedback)

        # === Gripper openen ===
        control_gripper(0)
        rospy.sleep(1)

        # === Ga terug naar home ===
        group.go(group.get_named_target_values("home"), wait=True)
        feedback.status = "Actie voltooid"
        server.publish_feedback(feedback)

        # === Geef resultaat terug ===
        result.success = True
        server.set_succeeded(result)

    except Exception as e:
        rospy.logerr("Fout in sorteeractie: %s", e)
        result.success = False
        server.set_aborted(result)

# === Initialisatie ===
rospy.init_node('sorteer_action_server')
moveit_commander.roscpp_initialize(sys.argv)
group = moveit_commander.MoveGroupCommander("arm")

# Maak TF buffer aan om objectposities te vinden via vision
tf_buffer = tf2_ros.Buffer(rospy.Duration(100.0))
tf_listener = tf2_ros.TransformListener(tf_buffer)

# === Start de action server ===
server = actionlib.SimpleActionServer('sorteer_actie', SorterenAction, sorteer_callback, auto_start=False)
server.start()
rospy.loginfo("[Action Server] Sorteer actie gestart.")
rospy.spin()

