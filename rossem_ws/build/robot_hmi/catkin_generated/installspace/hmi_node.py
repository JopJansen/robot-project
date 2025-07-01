#!/usr/bin/env python2
import rospy
from std_msgs.msg import String
import Tkinter as tk
from xarm_msgs.srv import GetErr  # Import service voor foutcontrole robot

class HMI:
    def __init__(self, master):
        self.master = master
        self.master.title("Robot HMI")
        self.emergency_stop = False

        # ROS publishers
        self.transport_pub = rospy.Publisher('/transportband/commando', String, queue_size=10)
        self.robot_pub = rospy.Publisher('/robot/commando', String, queue_size=10)
        self.status_pub = rospy.Publisher('/robot/status', String, queue_size=10)
        self.cmd_pub = rospy.Publisher('/robot/command', String, queue_size=10)

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



        # Start periodic check for fysieke robot-noodstop (elke seconde)
        self.error_check_timer = rospy.Timer(rospy.Duration(1.0), self.timer_check_error)

    # === Verzend status naar robot status topic
    def publish_status(self, status):
        self.status_pub.publish(status)

    # === Verzend commando naar robot command topic
    def publish_command(self, command):
        self.cmd_pub.publish(command)

    # === Update statuslampjes
    def update_lights(self, green=False, orange=False, red=False):
        self.green_light.config(bg="green" if green else "gray")
        self.orange_light.config(bg="orange" if orange else "gray")
        self.red_light.config(bg="red" if red else "gray")

    # === Schakel knoppen aan/uit op basis van noodstopstatus
    def update_buttons(self):
        state = tk.DISABLED if self.emergency_stop else tk.NORMAL
        self.start_once_btn.config(state=state)
        self.start_cont_btn.config(state=state)
        self.stop_btn.config(state=state)

    # === Start één cyclus
    def start_once(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="In bedrijf - 1 cyclus", bg="orange")
        self.publish_status("in_bedrijf_once")
        self.publish_command("start_once")
        self.update_lights(green=False, orange=True, red=False)
        self.transport_pub.publish("START")
        self.robot_pub.publish("START_CYCLUS")

    # === Start continue cyclus
    def start_continuous(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="In bedrijf - Continue", bg="orange")
        self.publish_status("in_bedrijf_continue")
        self.publish_command("start_continue")
        self.update_lights(green=False, orange=True, red=False)
        self.transport_pub.publish("START")
        self.robot_pub.publish("START_CYCLUS_CONTINUE")

    # === Stop de cyclus
    def stop_cycle(self):
        if self.emergency_stop:
            return
        self.status_label.config(text="Wacht op start", bg="green")
        self.publish_status("wacht")
        self.publish_command("stop")
        self.update_lights(green=True, orange=False, red=False)
        self.transport_pub.publish("STOP")
        self.robot_pub.publish("STOP")

    # === Reset noodstop en status
    def reset(self):
        self.emergency_stop = False
        self.status_label.config(text="Wacht op start", bg="green")
        self.publish_status("wacht")
        self.publish_command("reset")
        self.update_lights(green=True, orange=False, red=False)
        self.update_buttons()



    # === Centrale noodstop-functie
    def activate_emergency(self, msg="NOODSTOP"):
        self.emergency_stop = True
        self.status_label.config(text="FOUT - " + msg, bg="red")
        self.update_lights(green=False, orange=False, red=True)
        self.update_buttons()
        self.transport_pub.publish("NOODSTOP")
        self.robot_pub.publish("NOODSTOP")
        self.status_pub.publish("fout")
        self.cmd_pub.publish("emergency_stop")

    # === Timerfunctie: check elke seconde of de robot een foutstatus heeft (via GetErr)
    def timer_check_error(self, event):
        if not self.emergency_stop:
            try:
                rospy.wait_for_service('/xarm/get_err', timeout=0.5)
                get_err = rospy.ServiceProxy('/xarm/get_err', GetErr)
                resp = get_err()
                if resp.err_code != 0:
                    rospy.logerr("xArm fout gedetecteerd! Foutcode: {}".format(resp.err_code))
                    self.activate_emergency("Robotfout: {}".format(resp.err_code))
            except rospy.ServiceException as e:
                rospy.logerr("Service call failed: %s" % e)
            except rospy.ROSException:
                rospy.logwarn("Service niet beschikbaar (timeout)")

if __name__ == '__main__':
    rospy.init_node('hmi_node')
    root = tk.Tk()
    hmi = HMI(root)
    root.mainloop()
