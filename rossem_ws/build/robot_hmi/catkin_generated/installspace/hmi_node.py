#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
import Tkinter as tk
from std_msgs.msg import String

class HMI:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot HMI")
        self.emergency_stop = False
        self.transport_pub = rospy.Publisher('/transportband/commando', String, queue_size=10)
        self.robot_pub = rospy.Publisher('/robot/commando', String, queue_size=10)
        self.transport_status_sub = rospy.Subscriber('/transportband/status', String, self.transport_status_callback)


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
        self.robot_pub.publish("RESET")

        self.reset_btn = tk.Button(master, text="Reset", command=self.reset)
        self.reset_btn.pack(pady=5)

        self.emergency_btn = tk.Button(master, text="Noodstop", command=self.emergency, bg="red")
        self.emergency_btn.pack(pady=5)

        # ROS publishers
        self.status_pub = rospy.Publisher('/robot/status', String, queue_size=10)
        self.cmd_pub = rospy.Publisher('/robot/command', String, queue_size=10)

    def publish_status(self, status):
        self.status_pub.publish(status)

    def publish_command(self, command):
        self.cmd_pub.publish(command)

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
        self.publish_status("in_bedrijf_once")
        self.publish_command("start_once")
        self.update_lights(green=False, orange=True, red=False)
        self.transport_pub.publish("START")
        self.robot_pub.publish("START_CYCLUS")

    def start_continuous(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="In bedrijf - Continue", bg="orange")
        self.publish_status("in_bedrijf_continue")
        self.publish_command("start_continue")
        self.update_lights(green=False, orange=True, red=False)
        self.transport_pub.publish("START")
        self.robot_pub.publish("START_CYCLUS_CONTINUE")

    def stop_cycle(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="Wacht op start", bg="green")
        self.publish_status("wacht")
        self.publish_command("stop")
        self.update_lights(green=True, orange=False, red=False)
        self.transport_pub.publish("STOP")
        self.robot_pub.publish("STOP")

    def reset(self):
        self.emergency_stop = False
        self.status_label.config(text="Wacht op start", bg="green")
        self.publish_status("wacht")
        self.publish_command("reset")
        self.update_lights(green=True, orange=False, red=False)
        self.update_buttons()


    def emergency(self):
        self.emergency_stop = True
        self.status_label.config(text="FOUT - NOODSTOP", bg="red")
        self.publish_status("fout")
        self.publish_command("emergency_stop")
        self.update_lights(green=False, orange=False, red=True)
        self.update_buttons()
        self.transport_pub.publish("NOODSTOP")
        self.robot_pub.publish("NOODSTOP")
    

    def transport_status_callback(self, msg):
    	if msg.data == "ERROR":
           self.status_label.config(text="FOUT - Geen detectie bij sensor 2", bg="red")
           self.update_lights(green=False, orange=False, red=True)
           self.emergency_stop = True
           self.update_buttons()
           self.publish_status("fout")
           self.publish_command("voorwerp_verdwenen")
    	else:
           rospy.loginfo("Transport status ontvangen: %s", msg.data)



if __name__ == '__main__':
    rospy.init_node('hmi_node')
    root = tk.Tk()
    hmi = HMI(root)
    root.mainloop()

