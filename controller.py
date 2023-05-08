import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# Initialize I2C bus
i2c = busio.I2C(SCL, SDA)

# Create a simple PCA9685 class instance, set a frequency of 50hz
pca = PCA9685(i2c)
pca.frequency = 50

# Set up for servo #0
servo0_range = 180
servo0 = servo.Servo(pca.channels[0], actuation_range=servo0_range, min_pulse=490, max_pulse=1950)

# Statically hold the rest of the servos
servo1 = servo.Servo(pca.channels[1], actuation_range=135)
servo2 = servo.Servo(pca.channels[2], actuation_range=135)
servo3 = servo.Servo(pca.channels[3], actuation_range=135)
servo1.angle = 100
servo2.angle = 90
servo3.angle = 90

# We sleep in the loops to give the servo time to move into position.
for i in range(servo0_range):
    servo0.angle = i
    time.sleep(0.03)
# Wait before sweeping back
time.sleep(10)
for i in range(servo0_range):
    servo0.angle = servo0_range - i
    time.sleep(0.03)

# # You can also specify the movement fractionally.
# fraction = 0.0
# while fraction < 1.0:
#     servo7.fraction = fraction
#     fraction += 0.01
#     time.sleep(0.03)

# servo0.fraction = 0

pca.deinit()