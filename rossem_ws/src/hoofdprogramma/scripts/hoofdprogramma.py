#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Bool
from your_package.msg import VisionResponse, RobotGoal  # vervang 'your_package' naar je package
from geometry_msgs.msg import Pose2D


class Hoofdcontroller:
    def __init__(self):
        rospy.init_node('hoofdcontroller')

        # Publishers
        self.vision_trigger_pub = rospy.Publisher('/vision/request_scan', Bool, queue_size=1)
        self.robot_goal_pub = rospy.Publisher('/robot/goal', RobotGoal, queue_size=1)
        self.transportband_pub = rospy.Publisher('/transportband/commando', String, queue_size=1)
        self.coordinaten_pub = rospy.Publisher('/camera/coordinaten', Pose2D, queue_size=1)

        # Subscribers
        rospy.Subscriber('/hmi/input', String, self.hmi_callback)
        rospy.Subscriber('/transportband/status', String, self.transportband_status_callback)
        rospy.Subscriber('/vision/response', VisionResponse, self.vision_callback)
        rospy.Subscriber('/camera/detected_pose', Pose2D, self.camera_callback)

        self.transportband_ready = False
        self.awaiting_vision = False

        # Dummy publish zodat topic direct zichtbaar is
        dummy = Pose2D(x=0.0, y=0.0, theta=0.0)
        self.coordinaten_pub.publish(dummy)
        rospy.loginfo("Dummy Pose2D gepubliceerd op /camera/coordinaten zodat topic zichtbaar is")

        rospy.loginfo("Hoofdcontroller gestart")
        rospy.spin()

    def hmi_callback(self, msg):
        rospy.loginfo(f"HMI: {msg.data}")
        if msg.data == "START":
            rospy.loginfo("START ontvangen van HMI")
            self.transportband_pub.publish("START")

    def transportband_status_callback(self, msg):
        rospy.loginfo(f"Status transportband: {msg.data}")
        if msg.data == "READY":
            rospy.loginfo("Transportband is klaar, trigger vision scan")
            self.vision_trigger_pub.publish(True)
            self.awaiting_vision = True

    def vision_callback(self, msg):
        rospy.loginfo("Vision response ontvangen")

    def camera_callback(self, msg):
        rospy.loginfo(f"Pose ontvangen van camera: x={msg.x}, y={msg.y}, theta={msg.theta}")
        self.coordinaten_pub.publish(msg)
        rospy.loginfo("Pose doorgestuurd naar /camera/coordinaten")


if __name__ == '__main__':
    try:
        Hoofdcontroller()
    except rospy.ROSInterruptException:
        pass

