#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Pose2D, PoseStamped
import tf.transformations

class Hoofdcontroller:
    def __init__(self):
        rospy.init_node('hoofdcontroller')

        # Publishers
        self.vision_trigger_pub = rospy.Publisher('/vision/request_scan', Bool, queue_size=1)
        self.transportband_pub = rospy.Publisher('/transportband/commando', String, queue_size=1)
        self.coordinaten_pub = rospy.Publisher('/camera/coordinaten', Pose2D, queue_size=1)
        self.robot_pub = rospy.Publisher('/robot/starten', String, queue_size=1)  # Let op: String, niet Pose2D
        self.object_pose_pub = rospy.Publisher('/object_pose_world', PoseStamped, queue_size=1)
        self.vision_output_pub = rospy.Publisher('/vision_output', String, queue_size=1)
        self.camera_start_pub = rospy.Publisher('/camera/start', String, queue_size=1)

        # Subscribers
        rospy.Subscriber('/hmi/input', String, self.hmi_callback)
        rospy.Subscriber('/transportband/status', String, self.transportband_status_callback)
        rospy.Subscriber('/camera/detected_pose', PoseStamped, self.camera_callback)
        rospy.Subscriber('/camera/status', String, self.camera_status_callback)

        rospy.loginfo("Hoofdcontroller gestart")
        rospy.spin()

    def hmi_callback(self, msg):
        if msg.data.strip().upper() == "START":
            rospy.loginfo("START ontvangen van HMI -> start transportband")
            self.transportband_pub.publish("START")

    def transportband_status_callback(self, msg):
        if msg.data.strip().upper() == "READY":
            rospy.loginfo("Transportband is klaar -> trigger vision scan")
            self.vision_trigger_pub.publish(True)

    def camera_callback(self, msg):
        # Stuur de gedetecteerde pose door naar coordinaten_pub (indien nodig)
        pose2d = Pose2D()
        q = msg.pose.orientation
        euler = tf.transformations.euler_from_quaternion([q.x, q.y, q.z, q.w])
        yaw = euler[2]
        pose2d.x = msg.pose.position.x
        pose2d.y = msg.pose.position.y
        pose2d.theta = yaw

        self.coordinaten_pub.publish(pose2d)
        rospy.loginfo(f"Coördinaten camera: x={pose2d.x:.3f}, y={pose2d.y:.3f}, theta={pose2d.theta:.3f}")

        # **BELANGRIJK**: publiceer het originele PoseStamped op `/object_pose_world`
        self.object_pose_pub.publish(msg)

        # Stuur start commando naar sorteer client
        self.robot_pub.publish("START")
        rospy.loginfo("START bericht naar /robot/starten gestuurd voor sorteer client")

        # (optioneel) Stel een doelpositie in
        self.vision_output_pub.publish("inbus")  # of een andere doelpositie
        rospy.loginfo("Doelpositie 'inbus' naar /vision_output gestuurd")

    def camera_status_callback(self, msg):
        if msg.data.strip().lower() == "klaar":
            rospy.loginfo("Camera status 'klaar' ontvangen -> stuur START naar /camera/start")
            self.camera_start_pub.publish("START")


if __name__ == '__main__':
    try:
        Hoofdcontroller()
    except rospy.ROSInterruptException:
        pass
