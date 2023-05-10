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

def send_command(servo_num, servo_pos):
    command = f"{servo_num},{servo_pos}\n"
    ser.write(command.encode())

# Set up the serial connection
ser = serial.Serial('/dev/ttyACM0', 9600) # Change '/dev/ttyACM0' to the appropriate port for your system
time.sleep(2) # Wait for the connection to be established

# Set the initial servo positions
servo_positions = [90, 90, 90, 90, 90, 90]

# Define the keys for controlling the servos
servo_keys = {
    '7': (0, -10), 'u': (0, 10),
    '2': (1, -10), 'w': (1, 10),
    '3': (2, -10), 'e': (2, 10),
    '4': (3, -10), 'r': (3, 10),
    '5': (4, -10), 't': (4, 10),
    '6': (5, -10), 'y': (5, 10),
}

# Control the servos with the keyboard
print("Press the specified keys to control the servos. Press 'q' to exit.")
while True:
    key_name = getch()
    if key_name == 'q':
        break
    if key_name in servo_keys:
        servo_num, delta = servo_keys[key_name]
        servo_positions[servo_num] += delta
        servo_positions[servo_num] = min(max(servo_positions[servo_num], 0), 180)
        send_command(servo_num, servo_positions[servo_num])
        print(f"Servo {servo_num + 1}: {servo_positions[servo_num]}")

# Close the serial connection
ser.close()

