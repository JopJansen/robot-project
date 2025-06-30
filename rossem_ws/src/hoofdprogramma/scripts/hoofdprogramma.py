#!/usr/bin/env python
# -*- coding: utf-8 -*-
import rospy
import actionlib
from std_msgs.msg import String, Bool
from geometry_msgs.msg import Pose2D, PoseStamped
import tf.transformations
from robot_arm_pkg.msg import SorterenAction, SorterenGoal

class Hoofdcontroller:
    def __init__(self):
        # Initialiseer de ROS-node
        rospy.init_node('hoofdcontroller')

        # === Action client naar manipulator (SorterenAction) ===
        self.client = actionlib.SimpleActionClient('sorteer_actie', SorterenAction)
        rospy.loginfo("Wachten op manipulator action server...")
        self.client.wait_for_server()
        rospy.loginfo("Verbonden met manipulator action server.")

        # === Publishers: sturen commando's naar andere units ===
        self.vision_trigger_pub = rospy.Publisher('/vision/request_scan', Bool, queue_size=1)
        self.transportband_pub = rospy.Publisher('/transportband/commando', String, queue_size=1)
        self.coordinaten_pub = rospy.Publisher('/camera/coordinaten', Pose2D, queue_size=1)
        self.robot_pub = rospy.Publisher('/robot/starten', String, queue_size=1)
        self.camera_start_pub = rospy.Publisher('/camera/start', String, queue_size=1)

        # === Subscribers: ontvangen informatie van andere units ===
        #rospy.Subscriber('/hmi/input', String, self.hmi_callback)
        rospy.Subscriber('/transportband/status', String, self.transportband_status_callback)
        #rospy.Subscriber('/camera/detected_pose', PoseStamped, self.pose_callback)          # coordinaten vanuit camera
        rospy.Subscriber('/camera/status', String, self.camera_status_callback)
        rospy.Subscriber('/camera/detected_label', String, self.doelpositie_callback)     # doelbakje van vision
        rospy.Subscriber('/object_pose_world', PoseStamped, self.pose_callback)            # coordinaten vanuit transformer


        # === Statusbuffers ===
        self.started = True               # of het systeem begonnen is met sorteren
        self.laatste_pose = None            # laatst ontvangen objectpose (getransformeerd)
        self.laatste_doelpositie = None     # laatst ontvangen doelbakje van vision

        rospy.loginfo("Hoofdcontroller gestart.")
        rospy.spin()  # hou node actief

    # === CALLBACK: HMI geeft START-commando (bijv. knop ingedrukt) ===
    def hmi_callback(self, msg):
        rospy.loginfo("hmi_callback aangeroepen met data: %s" % msg.data)
        if msg.data.strip().upper() == "START":
            rospy.loginfo("START ontvangen van HMI -> transportband starten.")
            self.transportband_pub.publish("START")
            self.started = True  # systeem is nu actief

    # === CALLBACK: transportband is klaar, vision mag starten ===
    def transportband_status_callback(self, msg):
        if msg.data.strip().upper() == "READY":
            rospy.loginfo("Transportband status 'READY' -> trigger vision scan.")
            self.vision_trigger_pub.publish(True)

    # === CALLBACK: getransformeerde pose ontvangen van vision pipeline ===
    def pose_callback(self, msg):
        #rospy.loginfo(f"pose_callback: started={self.started}")
        rospy.loginfo("pose_callback aangeroepen")
        print("test")
        if not self.started:
            rospy.logwarn("Nog niet gestart – pose genegeerd.")
            return

        # Sla de laatste pose op
        self.laatste_pose = msg
        rospy.loginfo("Nieuwe objectpose ontvangen van /object_pose_world.")

        # Probeer goal naar manipulator te sturen
        self.verzend_sorteer_goal_als_klaar()

    # === CALLBACK: vision stuurt het doelbakje waarin gesorteerd moet worden ===
    def doelpositie_callback(self, msg):
        rospy.loginfo("doelpositie_callback aangeroepen")
        self.laatste_doelpositie = msg.data.strip()
        #rospy.loginfo(f"Nieuwe doelpositie ontvangen van vision: '{self.laatste_doelpositie}'")

        # Probeer goal naar manipulator te sturen
        self.verzend_sorteer_goal_als_klaar()

    # === CALLBACK: camera is klaar voor nieuwe opname ===
    def camera_status_callback(self, msg):
        rospy.loginfo("Camera status 'klaar' -> stuur START naar /camera/start")
        if msg.data.strip().lower() == "klaar":
            rospy.loginfo("OK - klaar ontvangen, stuur goal")
            

    # === Functie: stuur goal naar de manipulator als alle data binnen is ===
    def verzend_sorteer_goal_als_klaar(self):
        print ("mani started")
        #rospy.loginfo(f"verzend_sorteer_goal_als_klaar aangeroepen. started={self.started}, pose={self.laatste_pose is not None}, doelpositie={self.laatste_doelpositie}")
        if not self.started:
            rospy.logwarn("Nog niet gestart, goal niet verzonden.")
            return# Controleer of systeem gestart is
        if not self.started:
            return

        # Wacht op zowel een objectpose als een doelpositie
        if self.laatste_pose is None:
            rospy.loginfo("Wacht op objectpose van vision.")
            return

        if self.laatste_doelpositie is None:
            rospy.loginfo("Wacht op doelpositie van vision.")
            return

        # Bouw het goal op
        goal = SorterenGoal()
        goal.tf_frame = self.laatste_pose.header.frame_id   # meestal 'world'
        goal.doel_positie = self.laatste_doelpositie        # bv. 'inbus' of 'torx'

        # Stuur het goal naar de manipulator
        self.client.send_goal(goal, feedback_cb=self.feedback_cb)
        #rospy.loginfo(f"Goal verzonden: tf_frame='{goal.tf_frame}', doelpositie='{goal.doel_positie}'")

        # Reset buffers zodat er op nieuwe data gewacht wordt
        self.laatste_pose = None
        self.laatste_doelpositie = None

        # Stuur status naar andere systemen dat robot bezig is
        self.robot_pub.publish("START")

    # === CALLBACK: feedback van manipulator action server ===
    def feedback_cb(self, feedback):
        rospy.loginfo("Feedback van manipulator: " + feedback.status)


if __name__ == '__main__':
    try:
        Hoofdcontroller()
    except rospy.ROSInterruptException:
        pass
