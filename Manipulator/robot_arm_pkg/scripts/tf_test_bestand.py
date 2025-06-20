#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Deze regel zorgt dat het script als ROS-node uitgevoerd kan worden

import rospy  # ROS Python-bibliotheek
import tf2_ros  # TF2-bibliotheek voor transform-communicatie in ROS
import geometry_msgs.msg  # Berichttypes voor posities en oriëntaties

# Initialiseer de ROS-node met de naam 'tf_broadcaster'
rospy.init_node('tf_broadcaster')

# Maak een broadcaster-object aan dat transform-berichten uitzendt
br = tf2_ros.TransformBroadcaster()

# Stel de frequentie in op 10 Hz (10 keer per seconde)
rate = rospy.Rate(10)

# Deze lus blijft draaien zolang de node niet is afgesloten
while not rospy.is_shutdown():
    # Maak een nieuw TransformStamped-bericht aan
    t = geometry_msgs.msg.TransformStamped()

    # Zet de tijd op het huidige moment
    t.header.stamp = rospy.Time.now()

    # Geef aan dat deze transform ten opzichte van het 'world' frame is
    t.header.frame_id = "world"

    # De naam van het nieuwe coördinatenframe dat je maakt
    t.child_frame_id = "ik_testpoint"

    # Stel de positie in van het 'ik_testpoint'-frame t.o.v. 'world' (in meters)
    t.transform.translation.x = -0.09  # 50 cm naar voren
    t.transform.translation.y = -0.3  # Geen zijwaartse verplaatsing
    t.transform.translation.z = 0.30  # 20 cm omhoog

    # Stel de oriëntatie in als geen rotatie (identiteit quaternion)
    t.transform.rotation.x = 0.0
    t.transform.rotation.y = 0.0
    t.transform.rotation.z = 0.0
    t.transform.rotation.w = 1.0

    # Stuur de transform over ROS TF
    br.sendTransform(t)

    # Wacht tot de volgende cyclus
    rate.sleep()































