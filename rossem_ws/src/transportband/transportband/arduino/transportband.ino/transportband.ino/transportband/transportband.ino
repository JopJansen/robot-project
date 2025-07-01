#include <ros.h>
#include <std_msgs/String.h>

// ROS setup
ros::NodeHandle nh;
std_msgs::String str_msg;
char buffer[50];

void hmiCallback(const std_msgs::String& msg);
ros::Subscriber<std_msgs::String> hmi_sub("/transportband/commando", &hmiCallback);
ros::Publisher chatter("/transportband/status", &str_msg);

// Flags en status
volatile bool hmiStart = false;
bool motorAan = false;
bool noodstopActief = false;

// Pin configuratie
const int trigPin1 = 11;
const int echoPin1 = 12;
const int trigPin2 = 10;
const int echoPin2 = 9;
const int motorPin1 = 6;
const int motorPin2 = 5;
const int enablePin = 3;

const int detectieAfstand = 15;

// Timer
unsigned long motorStartTijd = 0;
const unsigned long motorTimeout = 5000;  // 5 seconden

// HMI Callback (ontvangt START en NOODSTOP)
void hmiCallback(const std_msgs::String& msg) {
  if (strcmp(msg.data, "START_ONCES") == 0 || strcmp(msg.data, "START_CONTINUE") == 0) {
    if (noodstopActief) {
      noodstopActief = false;
    }

    hmiStart = true;
    snprintf(buffer, sizeof(buffer), "HMI commando ontvangen: %s", msg.data);
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }
  else if (strcmp(msg.data, "NOODSTOP") == 0) {
    stopMotor();
    hmiStart = false;
    motorAan = false;
    noodstopActief = true;
    snprintf(buffer, sizeof(buffer), "NOODSTOP ontvangen, motor gestopt");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }
}




void setup() {
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(trigPin2, OUTPUT);
  pinMode(echoPin2, INPUT);

  pinMode(motorPin1, OUTPUT);
  pinMode(motorPin2, OUTPUT);
  pinMode(enablePin, OUTPUT);
  stopMotor();

  nh.initNode();
  nh.advertise(chatter);
  nh.subscribe(hmi_sub);

}

void loop() {
  int afstand1 = meetAfstand(trigPin1, echoPin1);
  int afstand2 = meetAfstand(trigPin2, echoPin2);

  // Starten alleen als geen noodstop
  if (!motorAan && hmiStart && afstand1 > 0 && afstand1 <= detectieAfstand && !noodstopActief) {
    startMotor();
    motorAan = true;
    motorStartTijd = millis();

    snprintf(buffer, sizeof(buffer), "Motor gestart: sensor 1 + START");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }

  // Stoppen bij sensor 2
  if (motorAan && afstand2 > 0 && afstand2 <= detectieAfstand) {
    stopMotor();
    motorAan = false;
    hmiStart = false;

    snprintf(buffer, sizeof(buffer), "ready");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }

  // Time-out
  if (motorAan && (millis() - motorStartTijd > motorTimeout)) {
    stopMotor();
    motorAan = false;
    hmiStart = false;

    snprintf(buffer, sizeof(buffer), "ERROR");
    str_msg.data = buffer;
    chatter.publish(&str_msg);
  }

  nh.spinOnce();
  delay(100);
}

int meetAfstand(int trigPin, int echoPin) {
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);

  long duration = pulseIn(echoPin, HIGH, 30000);  // max 30ms
  if (duration <= 0) return -1;

  int afstand = duration * 0.034 / 2;
  return afstand;
}

void startMotor() {
  digitalWrite(motorPin1, HIGH);
  digitalWrite(motorPin2, LOW);
  analogWrite(enablePin, 140);
}

void stopMotor() {
  delay(200);
  digitalWrite(motorPin1, LOW);
  digitalWrite(motorPin2, LOW);
  analogWrite(enablePin, 0);
}
