#!/usr/bin/env python

import rospy
import moveit_commander

rospy.init_node('check_planning_frame')
moveit_commander.roscpp_initialize([])

group = moveit_commander.MoveGroupCommander("manipulator")
print("Planning frame:", group.get_planning_frame())
