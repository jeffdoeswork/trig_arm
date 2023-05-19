#include <Stepper.h>

const int stepsPerRevolution = 2048; // Change this value for the specific motor you are using
const int motorPin1 = 8;
const int motorPin2 = 9;
const int motorPin3 = 10;
const int motorPin4 = 11;

Stepper myStepper(stepsPerRevolution, motorPin1, motorPin2, motorPin3, motorPin4);

void setup() {
  Serial.begin(9600);
  myStepper.setSpeed(10); // Set stepper motor speed
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    if (command == 'R') {
      myStepper.step(stepsPerRevolution);
    } else if (command == 'L') {
      myStepper.step(-stepsPerRevolution);
    }
  }
}

