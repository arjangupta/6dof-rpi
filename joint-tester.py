"""
This program tests the robot joints:
1. Joint movement range
2. Movement to specific position
3. Current position of all joints
The user can then specify the servo to test and which action to perform.
"""

import time
from board import SCL, SDA
import busio
from adafruit_motor import servo
from adafruit_pca9685 import PCA9685
import json

def init():
    # Initialize I2C bus
    i2c = busio.I2C(SCL, SDA)

    # Create a simple PCA9685 class instance, set a frequency of 50hz
    pca = PCA9685(i2c)
    pca.frequency = 50

    return pca

def load_robot_properties():
    # Load the JSON file that contains the servo calibration data
    with open("robot-properties.json", "r") as file:
        robot_properties = json.load(file)
    return robot_properties

def test_servo_range(pca: PCA9685, servo_num, min_pulse, max_pulse, servo_range):
    # Get the current position of the servo
    test_servo = servo.Servo(pca.channels[servo_num], actuation_range=servo_range, min_pulse=min_pulse, max_pulse=max_pulse)
    current_pos = test_servo.angle
    # Show the current position of the servo
    print("Current position of servo " + str(servo_num) + ": " + str(current_pos))

    # Sweep the servo from the current position to 0 degrees
    for i in range(int(current_pos), -1, -1):
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
    # Get servo calibration data in robot properties
    robot_properties = load_robot_properties()
    # Loop until the user exits
    while True:
        # Ask the user which servo to test, or exit
        servo_num = input("Enter the servo number to test (0-5), or 'exit' to exit: ")
        # If the user entered 'exit', exit the program
        if servo_num == "exit":
            break
        # Otherwise, check if we got an integer between 0-5, and ask the user if they would like to:
        # 1. Test the servo range (show current calibrated min/max pulse widths, but let the user specify them)
        # 2. Go to a specific angle of the servo
        # 3. Show current positions of all servos
        elif servo_num.isdigit() and int(servo_num) >= 0 and int(servo_num) <= 5:
            # Cast the servo number to an integer
            servo_num = int(servo_num)
            # Ask the user what they would like to do
            action = input("Enter 'range' to test the servo range, 'angle' to go to a specific angle, or 'positions' to show current positions of all servos: ")
            # Get the current min/max pulse widths & actuation range of the servo
            min_pulse = robot_properties["servo_list"][servo_num]["min_pulse"]
            max_pulse = robot_properties["servo_list"][servo_num]["max_pulse"]
            actuation_range = robot_properties["servo_list"][servo_num]["actuation_range"]
            # If the user entered 'range', test the servo range
            if action == "range":
                # Ask the user what the min/max pulse widths, and actuation range should be
                # If the user enters nothing, use the current min/max pulse widths
                user_min_pulse = input("Enter the min pulse width (in microseconds) of the servo, or press enter to use the current min pulse width (" + str(min_pulse) + "): ")
                if user_min_pulse != "":
                    min_pulse = int(user_min_pulse)
                user_max_pulse = input("Enter the max pulse width (in microseconds) of the servo, or press enter to use the current max pulse width (" + str(max_pulse) + "): ")
                if user_max_pulse != "":
                    max_pulse = int(user_max_pulse)
                user_actuation_range = input("Enter the actuation range (in degrees) of the servo, or press enter to use the current actuation range (" + str(actuation_range) + "): ")
                if user_actuation_range != "":
                    actuation_range = int(user_actuation_range)
                # Test the servo range
                test_servo_range(pca, servo_num, min_pulse, max_pulse, actuation_range)
            # If the user entered 'angle', go to a specific angle
            elif action == "angle":
                # Ask the user what angle to go to
                angle = input("Enter the angle to go to (0-180): ")
                # Go to the specified angle
                test_servo = servo.Servo(pca.channels[servo_num], actuation_range=actuation_range, min_pulse=min_pulse, max_pulse=max_pulse)
                test_servo.angle = int(angle)
            # If the user entered 'positions', show current positions of all servos
            elif action == "positions":
                # Loop through all servos
                for i in range(6):
                    # Get the current position of the servo
                    test_servo = servo.Servo(pca.channels[i], actuation_range=actuation_range, min_pulse=min_pulse, max_pulse=max_pulse)
                    current_pos = test_servo.angle
                    # Show the current position of the servo
                    print("Current position of servo " + str(i) + ": " + str(current_pos))
            # If the user entered something else, show an error message
            else:
                print("Invalid action, please try again.")
        else:
            print("Invalid servo number, please try again.")
    # Deinitialize the PCA9685
    pca.deinit()
    # Show exit message
    print("Exiting...")

if __name__ == "__main__":
    main()