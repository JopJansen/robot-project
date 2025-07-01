#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importeer de benodigde ROS Python-pakketten
import rospy
import tf2_ros
import tf2_geometry_msgs  # Nodig om PoseStamped te kunnen transformeren via tf2
from geometry_msgs.msg import PoseStamped  # Voor het ontvangen van de pose uit de camera

# === Toegevoegde functie om Y en Z te corrigeren ===
def fix_optical_pose(pose_msg):  # <-- toegevoegd
    fixed = PoseStamped()
    fixed.header = pose_msg.header

    # Positie corrigeren voor optical frame (Z naar beneden, Y naar beneden → spiegelen)
    fixed.pose.position.x = pose_msg.pose.position.x
    fixed.pose.position.y = -pose_msg.pose.position.y
    fixed.pose.position.z = pose_msg.pose.position.z

    # Oriëntatie nog niet aangepast (optioneel)
    fixed.pose.orientation = pose_msg.pose.orientation

    return fixed
# === Einde van toegevoegde functie ===

# === Callbackfunctie die wordt aangeroepen zodra er een nieuw bericht binnenkomt op /camera/detected_pose ===
def pose_callback(msg):
    try:
        # Haal de transform op van het frame van de camera naar het wereldframe
        transform = tf_buffer.lookup_transform(
            target_frame="world",
            source_frame=msg.header.frame_id,
            time=rospy.Time(0),
            timeout=rospy.Duration(1.0)
        )

        # === Pas Y- en Z-as aan vóór transformatie (toegevoegd) ===
        fixed_msg = fix_optical_pose(msg)  # <-- aangepaste regel
        transformed_pose = tf2_geometry_msgs.do_transform_pose(fixed_msg, transform)
        
         # Print de getransformeerde coördinaten
        rospy.loginfo("Getransformeerde pose:\n"
                      "x: %.3f\n"
                      "y: %.3f\n"
                      "z: %.3f" % (
                          transformed_pose.pose.position.x,
                          transformed_pose.pose.position.y,
                          transformed_pose.pose.position.z
                      ))

        # Log de getransformeerde pose naar de terminal
        rospy.loginfo("Getransformeerde pose in 'world':")
        rospy.loginfo(transformed_pose)

        # Publiceer de aangepaste pose
        pub_pose_world.publish(transformed_pose)
        rospy.loginfo("Pose gepubliceerd op /object_pose_world")

    except (tf2_ros.LookupException, tf2_ros.ExtrapolationException, tf2_ros.ConnectivityException) as e:
        rospy.logwarn("TF transformatie mislukt: %s", str(e))

# === Hoofdfunctie: wordt uitgevoerd als het script start ===
if __name__ == '__main__':
    rospy.init_node('pose_transformer')

    tf_buffer = tf2_ros.Buffer()
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    # Publisher
    pub_pose_world = rospy.Publisher("/object_pose_world", PoseStamped, queue_size=1)

    # Subscriber voor de camera-detected pose
    rospy.Subscriber("/camera/detected_pose", PoseStamped, pose_callback)

    rospy.spin()
