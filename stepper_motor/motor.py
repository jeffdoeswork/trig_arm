import serial
import sys
import time
import tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

# Set up the serial connection
ser = serial.Serial('/dev/ttyUSB0', 9600)  # Change this to the appropriate port for your Arduino Nano
time.sleep(2)  # Wait for the connection to be established

# Control the stepper motor with the keyboard
print("Press '1' and '2' to control the stepper motor. Press 'q' to exit.")
while True:
    key_name = getch()
    if key_name == 'q':
        break
    elif key_name == '1':
        ser.write(b'1')
        print("Left")
    elif key_name == '2':
        ser.write(b'2')
        print("Right")

# Close the serial connection
ser.close()
