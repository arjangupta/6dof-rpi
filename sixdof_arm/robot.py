"""
This class represents 6 degree of freedom robot arm.
"""

from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from .robot_joint import RobotJoint
import json

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
        # Initialize the robot joints
        self.joints = []
    
    def load_robot_properties(self):
        # Load the JSON file that contains the servo calibration data
        with open("robot-properties.json", "r") as file:
            robot_properties = json.load(file)
        return robot_properties