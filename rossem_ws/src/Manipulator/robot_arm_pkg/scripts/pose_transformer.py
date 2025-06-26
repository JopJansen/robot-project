#!/usr/bin/env python

# Importeer de benodigde ROS Python-pakketten
import rospy
import tf2_ros
import tf2_geometry_msgs  # Nodig om PoseStamped te kunnen transformeren via tf2
from geometry_msgs.msg import PoseStamped  # Voor het ontvangen van de pose uit de camera

# === Callbackfunctie die wordt aangeroepen zodra er een nieuw bericht binnenkomt op /camera/detected_pose ===
def pose_callback(msg):
    try:
        # Haal de transform op van het frame van de camera (bijv. 'oak_camera_rgb_camera_optical_frame')
        # naar het wereldframe (bijv. 'world' of 'base_link').
        # Deze transform wordt opgehaald op het laatst bekende tijdstip (rospy.Time(0))
        transform = tf_buffer.lookup_transform(
            target_frame="world",              # Doelframe waarin je de pose wilt hebben
            source_frame=msg.header.frame_id,  # Bronframe van de pose (de camera)
            time=rospy.Time(0),                # Gebruik de laatste bekende transform
            timeout=rospy.Duration(1.0)        # Geef max 1 seconde de tijd om de transform te vinden
        )

        # Transformeer de pose naar het wereldframe
        transformed_pose = tf2_geometry_msgs.do_transform_pose(msg, transform)

        # Log de getransformeerde pose naar de terminal
        rospy.loginfo("Getransformeerde pose in 'world':")
        rospy.loginfo(transformed_pose)

        pub_pose_world.publish(transformed_pose)
        rospy.loginfo("Pose gepubliceerd op /object_pose_world")

    # Foutafhandeling voor als de transform niet beschikbaar is
    except (tf2_ros.LookupException, tf2_ros.ExtrapolationException, tf2_ros.ConnectivityException) as e:
        rospy.logwarn("TF transformatie mislukt: %s", str(e))

# === Hoofdfunctie: wordt uitgevoerd als het script start ===
if __name__ == '__main__':
    # Initialiseer de ROS-node
    rospy.init_node('pose_transformer')

    # Maak een tf2-buffer aan voor het opslaan van transforms
    tf_buffer = tf2_ros.Buffer()

    # Maak een TransformListener aan om TF-transformaties op te vangen en beschikbaar te maken via tf_buffer
    tf_listener = tf2_ros.TransformListener(tf_buffer)

    # publisher 
    pub_pose_world = rospy.Publisher("/object_pose_world", PoseStamped, queue_size=1)
    # Abonneer op het topic waarop de camera PoseStamped-berichten publiceert
    # Elke keer dat er een nieuw bericht binnenkomt, wordt pose_callback aangeroepen
    rospy.Subscriber("/camera/coordinaten", PoseStamped, pose_callback)

    # Zorg ervoor dat het script actief blijft om berichten te blijven verwerken
    rospy.spin()
