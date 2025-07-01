#!/usr/bin/env python
# -*- coding: utf-8 -*-

import rospy
import actionlib
from std_msgs.msg import String, Bool
from geometry_msgs.msg import Pose2D, PoseStamped
from robot_arm_pkg.msg import SorterenAction, SorterenGoal

class Hoofdcontroller:
    def __init__(self):
        rospy.init_node('hoofdcontroller')

        # action server aanmaken
        self.client = actionlib.SimpleActionClient('sorteer_actie', SorterenAction)
        rospy.loginfo("Wachten op manipulator action server...")
        self.client.wait_for_server()
        rospy.loginfo("Verbonden met manipulator action server.")

        # publishers
        self.vision_trigger_pub = rospy.Publisher('/vision/request_scan', Bool, queue_size=1)
        self.transportband_pub = rospy.Publisher('/transportband/commando', String, queue_size=1)
        self.coordinaten_pub = rospy.Publisher('/camera/coordinaten', Pose2D, queue_size=1)
        self.robot_pub = rospy.Publisher('/robot/starten', String, queue_size=1)
        self.camera_start_pub = rospy.Publisher('/camera/start', String, queue_size=1)

        # subscribers 
        rospy.Subscriber('/transportband/status', String, self.transportband_status_callback)
        rospy.Subscriber('/camera/status', String, self.camera_status_callback)
        rospy.Subscriber('/camera/detected_label', String, self.doelpositie_callback)
        rospy.Subscriber('/object_pose_world', PoseStamped, self.pose_callback)
        rospy.Subscriber('/robot/status', String, self.robot_status_callback)
        rospy.Subscriber('/manipulator/klaar', String, self.sorter_feedback_cb)
        self.started = True
        self.laatste_pose = None
        self.laatste_doelpositie = None

        rospy.loginfo("Hoofdcontroller gestart.")
        rospy.spin()
    #start transportband
    def transportband_status_callback(self, msg):
        status = msg.data.strip().upper()
        if status == "START":
            rospy.loginfo("Transportband status 'START' ontvangen -> publiceer 'START_ONCES'")
            self.transportband_pub.publish("START_ONCES")

    #sensor 2 gedetecteerd start camera 
        elif status == "READY":
            rospy.loginfo("Transportband status 'READY' -> trigger vision scan.")
            self.vision_trigger_pub.publish(True)
        
    #camera gedetecteerd  
    def camera_status_callback(self, msg):
        rospy.loginfo("Camera status ontvangen: %s", msg.data)
        if msg.data.strip().lower() == "klaar":
            rospy.loginfo("Camera klaar voor nieuwe opname.")

    #place positie aansturen
    def pose_callback(self, msg):
        rospy.loginfo("pose_callback aangeroepen")
        if not self.started:
            rospy.logwarn("Nog niet gestart – pose genegeerd.")
            return

        self.laatste_pose = msg
        rospy.loginfo("Nieuwe objectpose ontvangen.")
        self.verzend_sorteer_goal_als_klaar()

    def doelpositie_callback(self, msg):
        rospy.loginfo("doelpositie_callback aangeroepen")
        self.laatste_doelpositie = msg.data.strip()
        self.verzend_sorteer_goal_als_klaar()
    
    #start continue 
    def sorter_feedback_cb(self, msg):
        if msg.data.strip().upper() == "ACTIE VOLTOOID":
            rospy.loginfo("Sorteeractie voltooid -> transportband opnieuw starten")
            self.transportband_pub.publish("START_CONTINUE")
            self.started = True

    #start transportband
    def transportband_status_callback(self, msg):
        status = msg.data.strip().upper()
        if status == "STOP":
            rospy.loginfo("Transportband status 'STOP' ontvangen ")
            self.transportband_pub.publish("STOP")

    #aansturen action server manipulator 
    def verzend_sorteer_goal_als_klaar(self):
        if not self.started:
            rospy.logwarn("Nog niet gestart, goal niet verzonden.")
            return

        if self.laatste_pose is None:
            rospy.loginfo("Wacht op objectpose van vision.")
            return

        if self.laatste_doelpositie is None:
            rospy.loginfo("Wacht op doelpositie van vision.")
            return

        goal = SorterenGoal()
        goal.tf_frame = self.laatste_pose.header.frame_id
        goal.doel_positie = self.laatste_doelpositie

        self.client.send_goal(goal, feedback_cb=self.feedback_cb)

        self.laatste_pose = None
        self.laatste_doelpositie = None

        self.robot_pub.publish("START")
   
    #feedback 
    def feedback_cb(self, feedback):
        try:
            rospy.loginfo("Feedback van manipulator: {}".format(feedback))
        except Exception as e:
            rospy.logwarn("Fout in feedback_cb: {}".format(e))
	
        # robot status callback
    def robot_status_callback(self, msg):
        rospy.loginfo("Robot status ontvangen: %s", msg.data)



if __name__ == '__main__':
    try:
        Hoofdcontroller()
    except rospy.ROSInterruptException:
        pass
