#!/usr/bin/env python
import rospy
from std_msgs.msg import String, Bool
from your_package.msg import VisionResponse, RobotGoal  # vervang met juiste package en msg-namen

class Hoofdcontroller:
    def __init__(self):
        rospy.init_node('hoofdcontroller')

        # Publishers
        self.vision_trigger_pub = rospy.Publisher('/vision/request_scan', Bool, queue_size=1)
        self.robot_goal_pub = rospy.Publisher('/robot/goal', RobotGoal, queue_size=1)
        self.transportband_pub = rospy.Publisher('/transportband/commando', String, queue_size=1)

        # Subscribers
        rospy.Subscriber('/hmi/input', String, self.hmi_callback)
        rospy.Subscriber('/transportband/status', String, self.transportband_status_callback)
        rospy.Subscriber('/vision/response', VisionResponse, self.vision_callback)

        self.transportband_ready = False
        self.awaiting_vision = False

        rospy.loginfo("Hoofdcontroller gestart")
        rospy.spin()

    def hmi_callback(self, msg):
        if msg.data == "START":
            rospy.loginfo("START ontvangen van HMI")
            self.transportband_pub.publish("START")

    def transportband_status_callback(self, msg):
        if msg.data == "READY":
            rospy.loginfo("Transportband is klaar, trigger vision scan")
            self.vision_trigger_pub.publish(True)
            self.awaiting_vision = True

    def vision_callback(self, msg):
        if not self.awaiting_vision:
            return

        rospy.loginfo(f"Vision data ontvangen: x={msg.x}, y={msg.y}, type={msg.tool_type}")
        robot_coords = self.bereken_robot_coords(msg.x, msg.y)

        goal = RobotGoal()
        goal.x = robot_coords[0]
        goal.y = robot_coords[1]
        goal.tool_type = msg.tool_type

        self.robot_goal_pub.publish(goal)
        rospy.loginfo(f"Robot opdracht verzonden: {goal}")
        self.awaiting_vision = False

    def bereken_robot_coords(self, x, y):
        # Voorbeeld: simpele offset conversie, pas dit aan naar jouw werkruimte
        base_offset_x = 100.0
        base_offset_y = 200.0
        schaal = 1.0  # pixels naar mm

        robot_x = base_offset_x + (x * schaal)
        robot_y = base_offset_y + (y * schaal)

        return (robot_x, robot_y)

if __name__ == '__main__':
    try:
        Hoofdcontroller()
    except rospy.ROSInterruptException:
        pass

