"""
This program tests the range of the servos.
The user can specify the servo to test. 
The program will then get the current position of the servo,
then it will sweep the servo from that position to 0 degrees, 
and then to 180 degrees.
The user can then specify the servo to test again, or exit the program.
"""

import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

def init():
    # Initialize I2C bus
    i2c = busio.I2C(SCL, SDA)

    # Create a simple PCA9685 class instance, set a frequency of 50hz
    pca = PCA9685(i2c)
    pca.frequency = 50

    return pca

def test_servo_range(pca, servo_num, min_pulse, max_pulse):
    # Get the current position of the servo
    servo_range = 180
    test_servo = servo.Servo(pca.channels[servo_num], actuation_range=servo_range, min_pulse=min_pulse, max_pulse=max_pulse)
    current_pos = servo.angle

    # Sweep the servo from the current position to 0 degrees
    for i in range(current_pos, -1, -1):
        test_servo.angle = i
        time.sleep(0.03)
    # Wait for 10 seconds
    time.sleep(10)
    # Sweep the servo from 0 degrees to 180 degrees
    for i in range(0, servo_range + 1):
        test_servo.angle = i
        time.sleep(0.03)

def main():
    # Initialize the PCA9685 and I2C bus
    pca = init()
    # Loop until the user exits
    while True:
        # Ask the user which servo to test, or exit
        servo_num = input("Enter the servo number to test (0-5), or 'exit' to exit: ")
        # If the user entered 'exit', exit the program
        if servo_num == "exit":
            break
        # Otherwise, ask for the minimum and maximum pulse widths to use
        else:
            # Get the minimum pulse width
            min_pulse = input("Enter the minimum pulse width (usually, 480-1970): ")
            # Get the maximum pulse width
            max_pulse = input("Enter the maximum pulse width (usually, 480-1970): ")
            # Convert the minimum and maximum pulse widths to integers
            min_pulse = int(min_pulse)
            max_pulse = int(max_pulse)
            # Convert the servo number to an integer
            servo_num = int(servo_num)
            # Test the servo range
            test_servo_range(pca, servo_num, min_pulse, max_pulse)
    # Deinitialize the PCA9685
    pca.deinit()
    # Show exit message
    print("Exiting...")

if __name__ == "__main__":
    main()