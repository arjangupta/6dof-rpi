"""
This class represents 6 degree of freedom robot arm.
"""

from board import SCL, SDA
import busio
from adafruit_pca9685 import PCA9685
from .robot_joint import RobotJoint
import json
import os
import time

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
    """
    Load the JSON file that contains the servo calibration data.
    :return: A dictionary containing the servo calibration data.
    """
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
    """
    Get the current positions of all joints.
    :return: A list containing the current positions of all joints.
    """
    def get_current_positions(self):
        # Get the current positions of all joints
        current_positions = []
        for joint in self.joints:
            current_positions.append(joint.current_angle)
        return current_positions
    """
    Move the robot arm to a target position.
    :param target_dict: A dictionary containing the target positions of all joints.
    """
    def move_to(self, target_dict):
        # Check if the target_dict contains all the joints, if they are not None, and if they are within the range of motion of the joint
        if "joint1" in target_dict and not target_dict["joint1"] is None and isinstance(target_dict["joint1"], int) and target_dict["joint1"] >= 0 and target_dict["joint1"] <= self.joints[0].angle_range:
            self.joints[0].set_destination(target_dict["joint1"])
        if "joint2" in target_dict and not target_dict["joint2"] is None and isinstance(target_dict["joint2"], int) and target_dict["joint2"] >= 0 and target_dict["joint2"] <= self.joints[1].angle_range:
            self.joints[1].set_destination(target_dict["joint2"])
        if "joint3" in target_dict and not target_dict["joint3"] is None and isinstance(target_dict["joint3"], int) and target_dict["joint3"] >= 0 and target_dict["joint3"] <= self.joints[2].angle_range:
            self.joints[2].set_destination(target_dict["joint3"])
        if "joint4" in target_dict and not target_dict["joint4"] is None and isinstance(target_dict["joint4"], int) and target_dict["joint4"] >= 0 and target_dict["joint4"] <= self.joints[3].angle_range:
            self.joints[3].set_destination(target_dict["joint4"])
        if "joint5" in target_dict and not target_dict["joint5"] is None and isinstance(target_dict["joint5"], int) and target_dict["joint5"] >= 0 and target_dict["joint5"] <= self.joints[4].angle_range:
            self.joints[4].set_destination(target_dict["joint5"])
        if "joint6" in target_dict and not target_dict["joint6"] is None and isinstance(target_dict["joint6"], int) and target_dict["joint6"] >= 0 and target_dict["joint6"] <= self.joints[5].angle_range:
            self.joints[5].set_destination(target_dict["joint6"])
        # Set direction of movement for each joint
        for joint in self.joints:
            if joint.current_angle < joint.destination:
                joint.direction_of_movement = 1
            else:
                joint.direction_of_movement = -1
        # Get the shortest sleep interval of all joints
        shortest_sleep_interval = min(joint.current_sweep_interval for joint in self.joints)
        # Move the joints toward their destinations
        while True:
            # Move each joint toward its destination
            for joint in self.joints:
                # Check the joint is at its destination and if it is time to move
                if not joint.is_at_destination() and time.monotonic() - joint.last_move_time >= joint.current_sweep_interval:
                    # Move the joint toward its destination
                    joint.move_toward_destination()
                    # Update the last move time
                    joint.last_move_time = time.monotonic()
                else:
                    # Set moving flag to False
                    joint.is_moving = False
            # Wait for the shortest sleep interval
            time.sleep(shortest_sleep_interval)
            # Check if all joints are at their destination
            if not any(joint.is_moving for joint in self.joints):
                break
