#!/usr/bin/env python
import rospy
from geometry_msgs.msg import PoseStamped

def publish_test_pose():
    rospy.init_node('test_pose_publisher', anonymous=True)
    pose_pub = rospy.Publisher('/camera/coordinaten', PoseStamped, queue_size=10)

    # Wacht tot er een subscriber is (optioneel, handig voor debugging)
    while pose_pub.get_num_connections() == 0 and not rospy.is_shutdown():
        rospy.loginfo("Wachten op subscriber...")
        rospy.sleep(0.1)

    # Maak de vaste pose
    pose_msg = PoseStamped()
    pose_msg.header.stamp = rospy.Time.now()
    pose_msg.header.frame_id = "oak_camera_rgb_camera_optical_frame"  # of 'world', afhankelijk van je TF-structuur

    # === Hier zet je je vaste coordinaten ===
    pose_msg.pose.position.x = -0.1
    pose_msg.pose.position.y = 0.0
    pose_msg.pose.position.z = 0.355
    pose_msg.pose.orientation.x = 0.0
    pose_msg.pose.orientation.y = 0.0
    pose_msg.pose.orientation.z = 0.0
    pose_msg.pose.orientation.w = 1.0

    # Publiceer eenmalig of in een loop
    rospy.loginfo("Publiceert test-coordinaten op /camera/detected_pose...")
    rate = rospy.Rate(1)  # 1 Hz
    while not rospy.is_shutdown():
        pose_msg.header.stamp = rospy.Time.now()  # Zorg dat de timestamp actueel blijft
        pose_pub.publish(pose_msg)
        rate.sleep()

if __name__ == '__main__':
    try:
        publish_test_pose()
    except rospy.ROSInterruptException:
        pass
