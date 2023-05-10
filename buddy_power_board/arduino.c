#include <Wire.h>
#include <Adafruit_PWMServoDriver.h>

Adafruit_PWMServoDriver pwm = Adafruit_PWMServoDriver();

void setup() {
  Serial.begin(9600);
  pwm.begin();
  pwm.setPWMFreq(60); // Set the PWM frequency for the servos
}

void setServoAngle(uint8_t channel, uint16_t angle) {
  uint16_t pulse = map(angle, 0, 180, 150, 600);
  pwm.setPWM(channel, 0, pulse);
}

void loop() {
  if (Serial.available()) {
    int servo_num = Serial.parseInt();
    int servo_pos = Serial.parseInt();

    if (servo_num >= 1 && servo_num <= 5 && servo_pos >= 0 && servo_pos <= 180) {
      setServoAngle(servo_num - 1, servo_pos);
    }
  }
}
