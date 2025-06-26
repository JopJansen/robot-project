#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def vision_callback(msg):
    """
    Verwacht input als: kleur:x,y
    Bijvoorbeeld: "rood:120,200"
    """
    data = msg.data.strip()
    kleur, coords = data.split(":")
    x, y = map(int, coords.split(","))

    # Doelcoördinaten op basis van kleur
    if kleur.lower() == "rode schroevendraaier":
        doel = "links_boven"
    elif kleur.lower() == "groene schroevendraaier":
        doel = "links_onder"
    elif kleur.lower() == "imbuus":
        doel = "rechts_boven"
    elif kleur.lower() == "doorzichtige schroevendraaier":
        doel = "rechts_onder"
    else:
        rospy.logwarn("Onbekende kleur: %s", kleur)
        return

    output = f"{kleur}:{x},{y} -> {doel}"
    rospy.loginfo("Omgezet: %s", output)
    output_pub.publish(output)

rospy.init_node('coordinaten_omzetter')
output_pub = rospy.Publisher('/coordinaten_output', String, queue_size=10)
rospy.Subscriber('/vision_output', String, vision_callback)
rospy.spin()

