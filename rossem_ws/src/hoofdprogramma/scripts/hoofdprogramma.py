#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
from std_msgs.msg import String, Bool
#from std_msgs.msg import VisionResponse, RobotGoal  # Pas aan naar juiste package
from geometry_msgs.msg import Pose2D, PoseStamped
import tf.transformations  # om quaternion naar euler te converteren


class Hoofdcontroller:
    def __init__(self):
        rospy.init_node('hoofdcontroller')

        # Publishers
        self.vision_trigger_pub = rospy.Publisher('/vision/request_scan', Bool, queue_size=1)
        #self.robot_goal_pub = rospy.Publisher('/robot/goal', RobotGoal, queue_size=1)
        self.transportband_pub = rospy.Publisher('/transportband/commando', String, queue_size=1)
        self.coordinaten_pub = rospy.Publisher('/camera/coordinaten', Pose2D, queue_size=1)

        # Subscribers
        rospy.Subscriber('/hmi/input', String, self.hmi_callback)
        rospy.Subscriber('/transportband/status', String, self.transportband_status_callback)
       # rospy.Subscriber('/vision/response', VisionResponse, self.vision_callback)
        rospy.Subscriber('/camera/detected_pose', PoseStamped, self.camera_callback)  # PoseStamped nu

        self.transportband_ready = False
        self.awaiting_vision = False

        rospy.loginfo("Hoofdcontroller gestart")
        rospy.spin()

    def hmi_callback(self, msg):
        if msg.data == "START":
            rospy.loginfo("START ontvangen van HMI")
            self.transportband_pub.publish("START")

    def transportband_status_callback(self, msg):
        if msg.data == "READY":
            rospy.loginfo("Transportband is klaar, trigger vision scan")
            self.vision_trigger_pub.publish(True)
            self.awaiting_vision = True

    def vision_callback(self, msg):
        rospy.loginfo("Vision response ontvangen")

    def camera_callback(self, msg):
        # Zet quaternion om naar yaw (theta)
        q = msg.pose.orientation
        euler = tf.transformations.euler_from_quaternion([q.x, q.y, q.z, q.w])
        yaw = euler[2]  # yaw

        # Zet PoseStamped om naar Pose2D met yaw
        pose2d = Pose2D()
        pose2d.x = msg.pose.position.x
        pose2d.y = msg.pose.position.y
        pose2d.theta = yaw

        rospy.loginfo("Coördinaten ontvangen van camera: x=%.3f, y=%.3f, theta=%.3f" % (pose2d.x, pose2d.y, pose2d.theta))
        self.coordinaten_pub.publish(pose2d)
        rospy.loginfo("Coördinaten doorgestuurd naar /camera/coordinaten")


if __name__ == '__main__':
    try:
        Hoofdcontroller()
    except rospy.ROSInterruptException:
        pass

