#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import rospy  # ROS Python-bibliotheek
import geometry_msgs.msg #import pose  # Berichttypes voor posities en oriëntaties
import moveit_commander               # Hoofdinterface met MoveIt


rospy.init_node('positie')

moveit_commander.roscpp_initialize(sys.argv)
robot = moveit_commander.RobotCommander()
scene = moveit_commander.PlanningSceneInterface()
group = moveit_commander.MoveGroupCommander('pos_end')             # Beheert de arm

pose = group.get_current_pose().pose

print("x:", pose.position.x)
print("y:", pose.position.y)
print("z:", pose.position.z)
print("qx:", pose.orientation.x)
print("qy:", pose.orientation.y)
print("qz:", pose.orientation.z)
print("qw:", pose.orientation.w)

