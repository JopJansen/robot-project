#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def callback(data):
    rospy.loginfo("Arduino zegt: %s", data.data)

def listener():
    rospy.init_node('arduino_listener')
    rospy.Subscriber("arduino_output", String, callback)
    rospy.spin()

if __name__ == '__main__':
    listener()

