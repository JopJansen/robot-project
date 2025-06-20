#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(msg):
    if msg.data == "START":
        rospy.loginfo("Transportband gestart")
        # Hier kan dan toegevoegd worden start transportband
    elif msg.data == "STOP":
        rospy.loginfo("Transportband gestopt")
        # Stop de motor
    elif msg.data == "NOODSTOP":
        rospy.loginfo("Transportband Noodstop")
        # Stop de motor

rospy.init_node('transportband_node')
rospy.Subscriber('/transportband/commando', String, callback)
rospy.spin()

