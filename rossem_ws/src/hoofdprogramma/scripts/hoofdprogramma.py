#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Bool
from your_package.msg import VisionResponse, RobotGoal  # vervang met juiste package en msg-namen
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


     def camera_callback(self, msg):
        rospy.loginfo(f"Coördinaten ontvangen van camera: x={msg.x}, y={msg.y}, theta={msg.theta}")
        self.coordinaten_pub.publish(msg)
        rospy.loginfo("Coördinaten doorgestuurd naar /camera/coordinaten")

if __name__ == '__main__':
    try:
        Hoofdcontroller()
    except rospy.ROSInterruptException:
        pass

