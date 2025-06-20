#!/usr/bin/env python

import rospy
from std_msgs.msg import String

emergency_active = False

def command_callback(msg):
    global emergency_active
    status = ""

    if msg.data == "emergency":
        emergency_active = True
        status = "noodstop"
    elif msg.data == "reset":
        emergency_active = False
        status = "stand-by"
    elif not emergency_active:
        if msg.data == "start":
            status = "start"
        elif msg.data == "stop":
            status = "stand-by"

    if status != "":
        rospy.loginfo("Status teruggestuurd: %s", status)
        pub_status.publish(status)

def transportband_callback(msg):
    rospy.loginfo("Transportband ontvangt commando: %s", msg.data)

def robot_cyclus_callback(msg):
    rospy.loginfo("Robot ontvangt cyclus-commando: %s", msg.data)

# Init node
rospy.init_node("robot_sim")

# Publishers
pub_status = rospy.Publisher("robot_status", String, queue_size=10)

# Subscribers
rospy.Subscriber("robot_command", String, command_callback)
rospy.Subscriber("/transportband/commando", String, transportband_callback)
rospy.Subscriber("/robot/commando", String, robot_cyclus_callback)

rospy.loginfo("robot_sim gestart. Wacht op HMI-commando's...")
rospy.spin()

