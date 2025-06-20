#include <ros.h>
#include <std_msgs/String.h>

// ROS NodeHandle en Publisher
ros::NodeHandle nh;
std_msgs::String str_msg;
ros::Publisher chatter("arduino_output", &str_msg);

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
char buffer[50];

void setup() {
  // Sensor pinnen
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  // Motor pinnen
  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);

  // Motor uitzetten
  stopMotor();

  // ROS initialisatie
  nh.initNode();
  nh.advertise(chatter);  

  // Opstartbericht
  snprintf(buffer, sizeof(buffer), "Systeem startklaar");
  str_msg.data = buffer;
  chatter.publish(&str_msg);
}

void loop() {
  int afstand1 = meetAfstand(trigPin1, echoPin1);
  int afstand2 = meetAfstand(trigPin2, echoPin2);

  if (!motorAan && afstand1 > 0 && afstand1 <= detectieAfstand) {
    startMotor();
    motorAan = true;
    snprintf(buffer, sizeof(buffer), "Motor gestart door sensor 1");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }

  if (motorAan && afstand2 > 0 && afstand2 <= detectieAfstand) {
    stopMotor();
    motorAan = false;
    snprintf(buffer, sizeof(buffer), "Motor gestopt door sensor 2");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }

  nh.spinOnce();
  delay(100);
}

int meetAfstand(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delay(2);
  digitalWrite(trigPin, HIGH);
  delay(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000);  // max 30 ms wachttijd
  if (duration <= 0) return -1;

  int afstand = duration * 0.034 / 2;
  return afstand;
}
 
void startMotor() {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW); 
  analogWrite(enablePin, 140);  // snelheid instellen
}

void stopMotor() {
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  analogWrite(enablePin, 0);
}
