#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Importeer ROS- en MoveIt-bibliotheken
import rospy                          # ROS-functionaliteit
import sys                            # Toegang tot command line-argumenten
import copy                           # Om objecten te kopiëren
import moveit_msgs.msg                # Berichten voor MoveIt
import geometry_msgs.msg              # Berichten voor posities en oriëntatie
import moveit_commander               # Hoofdinterface met MoveIt
from std_msgs.msg import Empty        # Leeg ROS-berichttype
import math                           # Wiskundige functies, zoals pi
import actionlib                      # Voor ROS Actions
from geometry_msgs.msg import Pose, Quaternion  # Specifieke ROS-berichten
from tf.transformations import *      # Functies om te draaien (rotaties)
import tf2_ros                        # TF2: voor coördinatentransformaties
import tf2_geometry_msgs              # TF2 voor geometrische berichten
from xarm_msgs.srv import SetInt16    # Voor gripper
 
# Start een ROS-node met naam 'test'
rospy.init_node('test')

# Maak een TF-buffer om posities van objecten op te vragen (max 100 sec oud)
tf_buffer = tf2_ros.Buffer(rospy.Duration(100.0))
tf_listener = tf2_ros.TransformListener(tf_buffer)

# Initialiseer MoveIt
moveit_commander.roscpp_initialize(sys.argv)
robot = moveit_commander.RobotCommander()                      # Algemene robotinfo
scene = moveit_commander.PlanningSceneInterface()              # Informatie over de omgeving
group = moveit_commander.MoveGroupCommander('arm')             # Beheert de arm

# Publisher om geplande paden te laten zien in RViz
display_trajectory_publisher = rospy.Publisher(
    '/move_group/display_planned_path',
    moveit_msgs.msg.DisplayTrajectory
)

#  Zet de vacuumgripper aan of uit
def control_gripper(state):

    rospy.wait_for_service('/ufactory/vacuum_gripper_set')
    try:
        gripper_service = rospy.ServiceProxy('/ufactory/vacuum_gripper_set',SetInt16)
        gripper_service(bool(state))
    except rospy.ServiceException as e:
        rospy.logerr("Vacuumgripper service call failed: %s", e)

def main():

	# === Naar 'home' positie gaan ===
	print("== ga naar home ==")
	target_values = group.get_named_target_values("home")          # Laad opgeslagen positie
	group.go(target_values, wait=True)                             # Beweeg ernaartoe

	# === gripper openen === 
	#control_gripper(0)
	#rospy.sleep(1)

	bak = [ "bak_rb","bak_lb","bak_lo","bak_ro"]

	for positie in bak:
		# === Naar positie van het vision-object gaan ===
		print("== ga naar test IK positie ==")
		transform = tf_buffer.lookup_transform('world', 'ik_testpoint', rospy.Time())  
		# Zoek positie van 'ik_testpoint' t.o.v. wereld

		# Zet TF transform om naar een Pose voor de robot
		destination_pose = Pose()
		destination_pose.position = transform.transform.translation
		destination_pose.orientation = transform.transform.rotation
	
		# Draai 180 graden om X-as zodat gripper goed staat
		q_orig = [transform.transform.rotation.x,
			  transform.transform.rotation.y,
			  transform.transform.rotation.z,
			  transform.transform.rotation.w]
	
		q_rot = quaternion_from_euler(math.pi, 0, 0)                    # Roteer over X-as
		q_new = quaternion_multiply(q_rot, q_orig)                     # Combineer rotaties	
	
		# Pas nieuwe rotatie toe aan transform
		transform.transform.rotation.x = q_new[0]
		transform.transform.rotation.y = q_new[1]
		transform.transform.rotation.z = q_new[2]
		transform.transform.rotation.w = q_new[3]
	
		# Zet aangepaste pose als doel voor de robot
		group.set_pose_target(destination_pose)
		plan = group.plan()
		group.go(wait=True)
		
	
		# === 5 cm omlaag bewegen ===
		print("== beweeg 5 cm omlaag ==")
		pose = group.get_current_pose()                                # Huidige positie ophalen
		posetarget = pose                                               # Kopie maken
		posetarget.pose.position.z -= 0.05                              # Z-waarde met 5 cm     		verlagen
		group.set_pose_target(posetarget)                              # Nieuwe positie instellen
		plan = group.plan()                                            # Pad plannen
		group.go(wait=True)                                            # Beweging uitvoeren

		# === gripper sluiten === 
		#control_gripper(1)
		#rospy.sleep(1)
	
		# === Naar 'stand_by' positie gaan ===
		print("== ga naar stand_by ==")
		target_values = group.get_named_target_values("stand_by")
		group.go(target_values, wait=True)
		rospy.sleep(1)


		# === Naar 'bak' positie gaan ===
		print("== ga naar " + positie + " ==")

		group.set_start_state_to_current_state()
		target_values = group.get_named_target_values(positie)
		group.go(target_values, wait=True)
		rospy.sleep(1)
	
		# === gripper openen === 
		#control_gripper(0)
		#rospy.sleep(1)
		
		# === Terug naar 'home' positie ===
		print("== ga naar home ==")
		target_values = group.get_named_target_values("home")
		group.go(target_values, wait=True)

	

	# === Terug naar 'home' positie ===
	print("== ga naar home ==")
	target_values = group.get_named_target_values("home")
	group.go(target_values, wait=True)



if __name__=='__main__':
	try:
		main()
	except rospy.ROSInterruptException:
		pass




