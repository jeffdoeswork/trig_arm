#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;

void setup() {
  Serial.begin(9600);

  servo1.attach(3);
  servo2.attach(5);
  servo3.attach(6);
  servo4.attach(9);
  servo5.attach(10);
}

void loop() {
  if (Serial.available()) {
    int servo_num = Serial.parseInt();
    int servo_pos = Serial.parseInt();

    if (servo_num >= 1 && servo_num <= 5 && servo_pos >= 0 && servo_pos <= 180) {
      switch (servo_num) {
        case 1: servo1.write(servo_pos); break;
        case 2: servo2.write(servo_pos); break;
        case 3: servo3.write(servo_pos); break;
        case 4: servo4.write(servo_pos); break;
        case 5: servo5.write(servo_pos); break;
      }
    }
  }
}
