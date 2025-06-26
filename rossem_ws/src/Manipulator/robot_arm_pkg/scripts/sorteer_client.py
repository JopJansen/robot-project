#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Importeer de benodigde ROS- en actie-libraries
import rospy
import actionlib
from geometry_msgs.msg import PoseStamped
from robot_arm_pkg.msg import SorterenAction, SorterenGoal  # Action definitie importeren

# === Callback functie die wordt aangeroepen zodra een nieuwe pose binnenkomt ===
def pose_cb(msg):
    # Log de ontvangen pose voor controle
    rospy.loginfo("Ontvangen objectpose in frame: %s", msg.header.frame_id)

    # Maak een nieuwe goal aan om naar de actionserver te sturen
    goal = SorterenGoal()
    goal.tf_frame = msg.header.frame_id      # Meestal 'world', dus vanaf wereld-coördinaten
    goal.doel_positie = "bak_rb"             # Hier geef je aan naar welke bak het object moet

    # Verstuur de goal naar de actionserver
    client.send_goal(goal, feedback_cb=feedback_cb)
    rospy.loginfo("Goal verzonden: object in '%s' -> sorteren naar '%s'",
                  goal.tf_frame, goal.doel_positie)

# === Callback functie die feedback afhandelt van de actionserver ===
def feedback_cb(feedback):
    rospy.loginfo("Feedback van robot: " + feedback.status)

# === Initialisatie van de ROS-node ===
rospy.init_node('sorteer_client')

# Maak een actionclient aan en verbind met de server met naam 'sorteer_actie'
client = actionlib.SimpleActionClient('sorteer_actie', SorterenAction)

# Wacht tot de server beschikbaar is
rospy.loginfo("Wachten op sorteer action server...")
client.wait_for_server()
rospy.loginfo("Verbonden met action server.")

# Abonneer op het topic waarop de getransformeerde pose wordt gepubliceerd
# Elke keer dat een nieuwe pose op /object_pose_world verschijnt, wordt pose_cb aangeroepen
rospy.Subscriber("/object_pose_world", PoseStamped, pose_cb)

# Houd de node actief om berichten te blijven ontvangen en verwerken
rospy.spin()
