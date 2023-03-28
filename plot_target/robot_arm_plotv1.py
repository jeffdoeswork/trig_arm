import math
import matplotlib.pyplot as plt
import serial
import time

# Add the following function to map angles to servo values
def map_angle_to_servo(angle, min_angle, max_angle, min_value, max_value):
    return int(((angle - min_angle) * (max_value - min_value) / (max_angle - min_angle)) + min_value)

# Replace '/dev/ttyACM0' with the appropriate port for your Arduino
arduino = serial.Serial('/dev/ttyACM0', 9600)
time.sleep(2)  # Give time for the connection to initialize

BASE_LEN = 0
ELBOW_LEN = 20
WRIST_LEN = 12

# Target coordinates in inches
target_x = 20
target_y = 3

# Calculate the angle between the base and the target point
base_angle = math.atan2(target_y, target_x)

# Calculate the distance between the base and elbow points
d = math.sqrt(target_x**2 + target_y**2) - BASE_LEN

# Calculate the angle between the elbow and the wrist points
cos_angle = (d**2 + ELBOW_LEN**2 - WRIST_LEN**2) / (2*d*ELBOW_LEN)
elbow_angle = math.acos(cos_angle)

# Calculate the endpoint of the elbow
elbow_x = BASE_LEN + ELBOW_LEN * math.cos(base_angle + elbow_angle)
elbow_y = ELBOW_LEN * math.sin(base_angle + elbow_angle)

# Calculate the endpoint of the wrist
wrist_angle = math.atan2(target_y - elbow_y, target_x - elbow_x)
wrist_x = elbow_x + WRIST_LEN * math.cos(wrist_angle)
wrist_y = elbow_y + WRIST_LEN * math.sin(wrist_angle)

# Plot the target point
plt.plot(target_x, target_y, 'ro')

# Plot the robot arm
plt.plot([BASE_LEN, elbow_x], [0, elbow_y], 'b-')
plt.plot([elbow_x, wrist_x], [elbow_y, wrist_y], 'b-')

# Set the axis limits
plt.xlim(-30, 40)
plt.ylim(-30, 30)

print(f"Base angle: {base_angle:.2f} degrees", base_angle)
print(f"Elbow angle: {elbow_angle:.2f} degrees", elbow_angle)
print("Base angle: ", math.degrees(base_angle))
print("Elbow angle: ", math.degrees(elbow_angle))
# Display the plot
plt.show()

# Convert the angles to degrees
base_angle_deg = math.degrees(base_angle)
elbow_angle_deg = math.degrees(elbow_angle)

# Map the angles to servo values (assuming servos have a range of 0 to 180 degrees)
servo1_value = map_angle_to_servo(base_angle_deg, 0, 180, 0, 180)
servo2_value = map_angle_to_servo(elbow_angle_deg, 0, 180, 0, 180)

# Send the servo values to the Arduino
arduino.write(f's1{servo1_value},s2{servo2_value}\n'.encode())

# Close the Arduino connection
arduino.close()