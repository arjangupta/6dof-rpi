"""
This file defines the RobotJoint class, which is used to control a single joint of the robot arm.
"""

from adafruit_motor import servo
import time

class RobotJoint:
    """
    Constructor for the RobotJoint class.
    :param pca: The PCA9685 object that controls the servo.
    :param joint_num: The number of the joint to control (1-6). Traditionally the first joint starts at index 1.
    :param angle_range: The range of motion of the joint in degrees.
    :param min_pulse: The minimum pulse width of the servo in microseconds.
    :param max_pulse: The maximum pulse width of the servo in microseconds.
    """
    def __init__(self, pca, joint_num, angle_range, min_pulse, max_pulse) -> None:
        self._pca = pca
        self.servo = servo.Servo(pca.channels[joint_num-1],actuation_range=angle_range, min_pulse=min_pulse, max_pulse=max_pulse)
        self.joint_num = joint_num
        self.angle_range = angle_range
        self.min_pulse = min_pulse
        self.max_pulse = max_pulse
        self.current_angle = self.servo.angle
        self.destination = self.current_angle
        self.current_sweep_interval = 0.02
        self.direction_of_movement = 1
        self.is_moving = False
    
    """
    Sets a destination angle for the joint to move to.
    :param angle: The destination angle for the joint to move to.
    """
    def set_destination(self, angle):
        # Check if the angle is within the range of motion of the joint
        if angle < 0 or angle > self.angle_range:
            print(f"Angle of {angle} given to joint #{self.joint_num} is out of range.")
            return
        self.destination = angle
        # Check direction of movement
        if self.current_angle < self.destination:
            self.direction_of_movement = 1
        else:
            self.direction_of_movement = -1
    
    """
    Set angular speed as a sweep interval for the joint to move to its destination.
    :param iteration_interval: The time interval between each iteration of the sweep.
    """
    def set_sweep_interval(self, iteration_interval):
        self.current_sweep_interval = iteration_interval
    
    """
    Move the joint toward its destination.
    """
    def move_toward_destination(self):
        # Set moving flag
        self.is_moving = True
        # Change current angle
        self.current_angle += self.direction_of_movement
        self.servo.angle = self.current_angle
    
    """
    Check if the joint is at its destination (within a tolerance of 1 degree)
    :return: True if the joint is at its destination, False otherwise.
    """
    def is_at_destination(self) -> bool:
        # Check if the joint is within a tolerance of 1 degree of its destination
        return self.current_angle >= self.destination - 1 and self.current_angle <= self.destination + 1

    """
    Get value of the moving flag.
    :return: True if the joint is moving, False otherwise.
    """
    def get_is_moving(self) -> bool:
        return self.is_moving
    
    """
    Get the current angle of the joint.
    :return: The current angle of the joint.
    """
    def get_current_angle(self) -> float:
        return self.current_angle