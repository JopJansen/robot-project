#!/usr/bin/env python
import rospy
import actionlib  # Nodig voor ROS Actions
from robot_arm_pkg.msg import SorterenAction, SorterenGoal  # Actietypes importeren

# Feedback callback functie: dit wordt aangeroepen als de server feedback stuurt
def feedback_cb(feedback):
    rospy.loginfo("Feedback van robot: " + feedback.status)

# === Start de ROS node ===
rospy.init_node('sorteer_client')

# Maak de client aan en verbind met de juiste servernaam
client = actionlib.SimpleActionClient('sorteer_actie', SorterenAction)

rospy.loginfo(" Wachten op action server...")
client.wait_for_server()  # Wacht tot de server is gestart

# === Stuur een opdracht (goal) naar de server ===
goal = SorterenGoal()
goal.tf_frame = "ik_testpoint"        # TF-frame van het object dat opgepakt moet worden
goal.doel_positie = "bak_rb"          # Naam van de sorteerbak (zoals opgeslagen in MoveIt)

rospy.loginfo(" Verzend opdracht aan robot...")
client.send_goal(goal, feedback_cb=feedback_cb)  # Stuur goal en koppel feedback functie

rospy.loginfo(" Wachten tot taak voltooid is...")
client.wait_for_result()  # Wacht tot robot klaar is

# === Resultaat controleren ===
resultaat = client.get_result()
if resultaat.success:
    rospy.loginfo(" Robot heeft het object succesvol gesorteerd.")
else:
    rospy.logwarn(" Sorteren is mislukt.")

