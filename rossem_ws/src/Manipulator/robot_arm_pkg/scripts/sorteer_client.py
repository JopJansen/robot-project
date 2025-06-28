#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from geometry_msgs.msg import PoseStamped
from robot_arm_pkg.msg import SorterenAction, SorterenGoal
from std_msgs.msg import String

laatste_doelpositie = "inbus"
started = False  # nieuwe globale vlag

def pose_cb(msg):
    global started
    if not started:
        rospy.loginfo("Wacht op START-commando voordat poses worden verwerkt.")
        return

    rospy.loginfo("Ontvangen objectpose in frame: %s", msg.header.frame_id)

    goal = SorterenGoal()
    goal.tf_frame = msg.header.frame_id
    goal.doel_positie = laatste_doelpositie

    client.send_goal(goal, feedback_cb=feedback_cb)
    rospy.loginfo("Goal verzonden: object in '%s' -> sorteren naar '%s'",
                  goal.tf_frame, goal.doel_positie)

def doelpositie_cb(msg):
    global laatste_doelpositie
    laatste_doelpositie = msg.data
    rospy.loginfo("Ontvangen doelpositie: %s", laatste_doelpositie)

def start_cb(msg):
    global started
    print ('testennnn')
    if msg.data == "START":
        started = True
        rospy.loginfo("START-commando ontvangen — sorteer_client is actief.")

def feedback_cb(feedback):
    rospy.loginfo("Feedback van robot: " + feedback.status)

if __name__ == '__main__':
    rospy.init_node('sorteer_client')

    client = actionlib.SimpleActionClient('sorteer_actie', SorterenAction)

    rospy.loginfo("Wachten op sorteer action server...")
    client.wait_for_server()
    rospy.loginfo("Verbonden met action server.")

    # abonneer op de relevante topics
    rospy.Subscriber("/object_pose_world", PoseStamped, pose_cb)
    rospy.Subscriber("/vision_output", String, doelpositie_cb)
    rospy.Subscriber("/robot/starten", String, start_cb)

    rospy.spin()

