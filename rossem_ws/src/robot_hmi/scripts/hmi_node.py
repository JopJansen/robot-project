#!/usr/bin/env python
import rospy
import Tkinter as tk
from std_msgs.msg import String, Bool
from xarm_msgs.msg import RobotMsg 
from xarm_msgs.srv import ClearErr  

class HMI:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot HMI")
        self.emergency_stop = False

        # Publishers
        self.transport_pub = rospy.Publisher('/transportband/commando', String, queue_size=10)
        self.robot_pub = rospy.Publisher('/robot/commando', String, queue_size=10)
        self.status_pub = rospy.Publisher('/robot/status', String, queue_size=10)
        self.cmd_pub = rospy.Publisher('/robot/command', String, queue_size=10)

        # Subscribers
        self.transport_status_sub = rospy.Subscriber('/transportband/status', String, self.transport_status_callback)
        self.camera_status_sub = rospy.Subscriber('camera/error', String, self.camera_status_callback)
        self.robot_state_sub = rospy.Subscriber('/ufactory/robot_states', RobotMsg, self.robot_state_callback)
        self.external_estop_sub = rospy.Subscriber('/custom/emergency_stop', Bool, self.external_estop_callback)

        # Status label
        self.status_label = tk.Label(master, text="Wacht op start", width=30, height=2, bg="green")
        self.status_label.pack(pady=10)

        # Status lampjes
        self.green_light = tk.Label(master, text="Wacht", width=30, height=2, bg="gray")
        self.orange_light = tk.Label(master, text="In bedrijf", width=30, height=2, bg="gray")
        self.red_light = tk.Label(master, text="Fout", width=30, height=2, bg="gray")

        self.green_light.pack(pady=2)
        self.orange_light.pack(pady=2)
        self.red_light.pack(pady=2)

        # Knoppen
        self.start_once_btn = tk.Button(master, text="Start 1 Cyclus", command=self.start_once)
        self.start_once_btn.pack(pady=5)

        self.start_cont_btn = tk.Button(master, text="Start Continue", command=self.start_continuous)
        self.start_cont_btn.pack(pady=5)

        self.stop_btn = tk.Button(master, text="Stop", command=self.stop_cycle)
        self.stop_btn.pack(pady=5)

        self.reset_btn = tk.Button(master, text="Reset", command=self.reset)
        self.reset_btn.pack(pady=5)

        # Start met RESET commando
        self.robot_pub.publish("RESET")

        # Zet start status
        self.update_lights(green=True, orange=False, red=False)
        self.update_buttons()

    def activate_emergency(self, msg="NOODSTOP"):
        rospy.logwarn("Noodstop geactiveerd: {}".format(msg))
        self.emergency_stop = True
        self.status_label.config(text="FOUT - " + msg, bg="red")
        self.update_lights(green=False, orange=False, red=True)
        self.update_buttons()
        self.transport_pub.publish("NOODSTOP")
        self.robot_pub.publish("NOODSTOP")
        self.status_pub.publish("fout")
        self.cmd_pub.publish("emergency_stop")


    def update_lights(self, green=False, orange=False, red=False):
        self.green_light.config(bg="green" if green else "gray")
        self.orange_light.config(bg="orange" if orange else "gray")
        self.red_light.config(bg="red" if red else "gray")

    def update_buttons(self):
        state = tk.DISABLED if self.emergency_stop else tk.NORMAL
        self.start_once_btn.config(state=state)
        self.start_cont_btn.config(state=state)
        self.stop_btn.config(state=state)

    def start_once(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="In bedrijf - 1 cyclus", bg="orange")
        self.status_pub.publish("in_bedrijf_once")
        self.cmd_pub.publish("start_once")
        self.update_lights(green=False, orange=True, red=False)
        self.transport_pub.publish("START_ONCES")
        self.robot_pub.publish("START_CYCLUS")

    def start_continuous(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="In bedrijf - Continue", bg="orange")
        self.status_pub.publish("in_bedrijf_continue")
        self.cmd_pub.publish("start_continue")
        self.update_lights(green=False, orange=True, red=False)
        self.transport_pub.publish("START_CONTINUE")
        self.robot_pub.publish("START_CYCLUS_CONTINUE")

    def stop_cycle(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="Wacht op start", bg="green")
        self.status_pub.publish("wacht")
        self.cmd_pub.publish("stop")
        self.update_lights(green=True, orange=False, red=False)
        self.transport_pub.publish("STOP")
        self.robot_pub.publish("STOP")

    def reset(self):
        rospy.loginfo("Reset actie gestart")
        self.emergency_stop = False
        self.status_label.config(text="Wacht op start", bg="green")
        self.status_pub.publish("wacht")
        self.cmd_pub.publish("reset")
        self.update_lights(green=True, orange=False, red=False)
        self.update_buttons()

    # Reset de noodstop via de service
    try:
        rospy.wait_for_service('/ufactory/moveit_clear_err', timeout=2.0)
        clear_warn_srv = rospy.ServiceProxy('/ufactory/moveit_clear_err', ClearErr)
        clear_warn_resp = clear_warn_srv()
        rospy.loginfo("Clear warn response: ret={}".format(clear_warn_resp.ret))
    except (rospy.ServiceException, rospy.ROSException) as e:
        rospy.logwarn("Kon moveit_clear_err service niet aanroepen: {}".format(e))


    def robot_state_callback(self, msg):
        # rospy.logwarn('Robot error status: {}'.format(msg.err))
        if msg.err == 2 and not self.emergency_stop:
            rospy.logwarn('Robot emergency stop (err=2) gedetecteerd via /ufactory/robot_states.')
            self.activate_emergency("Robot interne noodstop")

    def external_estop_callback(self, msg):
        rospy.logwarn("Externe noodstop bericht ontvangen")
        if msg.data:  # True = noodstop actief
            if not self.emergency_stop:
                self.activate_emergency("Externe noodstop")
        else:
            # Noodstop opgeheven
            if self.emergency_stop:
                rospy.loginfo("Noodstop opgeheven via extern signaal")
                self.reset()

    def transport_status_callback(self, msg):
        if msg.data == "ERROR":
            self.activate_emergency("Geen detectie bij sensor 2")
        else:
            rospy.loginfo("Transport status ontvangen: %s", msg.data)

    def camera_status_callback(self, msg):
        if msg.data == "no_detection":
            self.activate_emergency("Voorwerp niet gevonden")
        else:
            rospy.loginfo("Camera status ontvangen: %s", msg.data)


if __name__ == '__main__':
    rospy.init_node('hmi_node')
    root = tk.Tk()
    hmi = HMI(root)
    root.mainloop()
