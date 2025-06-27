#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
        doel = "bak_rb"
    elif kleur.lower() == "groene schroevendraaier":
        doel = "bak_lb"
    elif kleur.lower() == "inbus":
        doel = "bak_ro"
    elif kleur.lower() == "doorzichtige schroevendraaier":
        doel = "bak_lo"
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

