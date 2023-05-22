"""
This class represents 6 degree of freedom robot arm.
"""

from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from .robot_joint import RobotJoint
import json
import os

class Robot:
    """
    Constructor for the Robot class.
    """
    def __init__(self) -> None:
        # Initialize I2C bus
        i2c_bus = busio.I2C(SCL, SDA)
        # Create a simple PCA9685 class instance, set a frequency of 50hz
        print("Initializing PCA9685...")
        self.pca = PCA9685(i2c_bus)
        self.pca.frequency = 50 # TODO: Tune this from Adafruit's example code
        # Load the JSON robot properties file
        print("Loading robot properties...")
        self.robot_properties = self.load_robot_properties()
        # Get properties of the each servo
        servo_list = self.robot_properties["servo_list"]
        servo0 = servo_list[0]
        servo1 = servo_list[1]
        servo2 = servo_list[2]
        servo3 = servo_list[3]
        servo4 = servo_list[4]
        servo5 = servo_list[5]
        # Initialize the robot joints
        self.joints = [
            RobotJoint(self.pca, 1, servo0["actuation_range"], servo0["min_pulse"], servo0["max_pulse"]),
            RobotJoint(self.pca, 2, servo1["actuation_range"], servo1["min_pulse"], servo1["max_pulse"]),
            RobotJoint(self.pca, 3, servo2["actuation_range"], servo2["min_pulse"], servo2["max_pulse"]),
            RobotJoint(self.pca, 4, servo3["actuation_range"], servo3["min_pulse"], servo3["max_pulse"]),
            RobotJoint(self.pca, 5, servo4["actuation_range"], servo4["min_pulse"], servo4["max_pulse"]),
            RobotJoint(self.pca, 6, servo5["actuation_range"], servo5["min_pulse"], servo5["max_pulse"])
        ]
    def load_robot_properties(self):
        # Load the JSON file that contains the servo calibration data
        # If the file is not found, notify, show current directory and exit
        current_dir = os.getcwd()
        try:
            with open(current_dir + '/robot-properties.json') as f:
                robot_properties = json.load(f)
        except FileNotFoundError:
            print("robot-properties.json not found in current directory.")
            print("Current directory is:")
            print(current_dir)
            exit()
        return robot_properties
    def get_current_positions(self):
        # Get the current positions of all joints
        current_positions = []
        for joint in self.joints:
            current_positions.append(joint.current_angle)
        return current_positions