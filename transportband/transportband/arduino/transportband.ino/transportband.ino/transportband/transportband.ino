#include <ros.h>
#include <std_msgs/String.h>

// Globale ROS-objecten en status
ros::NodeHandle nh;
std_msgs::String str_msg;
char buffer[50];  // Globale buffer voor ROS-berichten

// Functievoorwaartse declaratie
void hmiCallback(const std_msgs::String& msg);

// ROS-subscriber op het juiste topic 
ros::Subscriber<std_msgs::String> hmi_sub("/transportband/commando", &hmiCallback);
ros::Publisher chatter("arduino_output", &str_msg);

// Startstatus ontvangen van HMI
volatile bool hmiStart = false;

// Sensor- en motorpinnen
const int trigPin1 = 11;
const int echoPin1 = 12;
const int trigPin2 = 10;
const int echoPin2 = 9;

const int motorPin1 = 6;
const int motorPin2 = 5;
const int enablePin = 3;

const int detectieAfstand = 15;
bool motorAan = false;

// Callback voor ontvangen HMI-commando's
void hmiCallback(const std_msgs::String& msg) {
  if (strcmp(msg.data, "START") == 0) {  // Hoofdlettergevoelig zoals HMI zendt
    hmiStart = true;
    snprintf(buffer, sizeof(buffer), "HMI commando ontvangen: START");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }
}

void setup() {
  // Sensor pinnen instellen
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  // Motor pinnen instellen
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);

  stopMotor();  // Motor uit bij opstart

  // ROS initialisatie
  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(hmi_sub);

  snprintf(buffer, sizeof(buffer), "Wacht op startcommando via /transportband/commando");
  str_msg.data = buffer;
  chatter.publish(&str_msg);
}

void loop() {
  int afstand1 = meetAfstand(trigPin1, echoPin1);
  int afstand2 = meetAfstand(trigPin2, echoPin2);

  // Start motor bij sensor 1 detectie én HMI "START"
  if (!motorAan && hmiStart && afstand1 > 0 && afstand1 <= detectieAfstand) {
    startMotor();
    motorAan = true;
    snprintf(buffer, sizeof(buffer), "Motor gestart: sensor 1 + HMI START");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }

  // Stop motor bij sensor 2 detectie
  if (motorAan && afstand2 > 0 && afstand2 <= detectieAfstand) {
    stopMotor();
    motorAan = false;
    hmiStart = false;  // Reset voor volgende cyclus
    snprintf(buffer, sizeof(buffer), "Motor gestopt: sensor 2 detectie");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }

  nh.spinOnce();
  delay(100);
}

// Ultrasoon afstand meten
int meetAfstand(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000);  // max 30 ms
  if (duration <= 0) return -1;

  int afstand = duration * 0.034 / 2;
  return afstand;
}

// Motor aanzetten
void startMotor() {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  analogWrite(enablePin, 140);  // snelheid
}

// Motor uitzetten
void stopMotor() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  analogWrite(enablePin, 0);
}
