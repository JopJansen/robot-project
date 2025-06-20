#!/usr/bin/env python

import rospy
from xarm_msgs.srv import SetInt16

rospy.init_node('gripper_control_node')

#  Zet de vacuumgripper aan of uit
def control_gripper(state):

    rospy.wait_for_service('/ufactory/vacuum_gripper_set')
    try:
        gripper_service = rospy.ServiceProxy('/ufactory/vacuum_gripper_set',SetInt16)
        gripper_service(bool(state))
    except rospy.ServiceException as e:
        rospy.logerr("Vacuumgripper service call failed: %s", e)


control_gripper(1)
rospy.sleep(1)
