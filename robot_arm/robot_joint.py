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
    
    """
    Lock on mutex, then set angular speed as a sweep interval for the joint to move to its destination.
    :param iteration_interval: The time interval between each iteration of the sweep.
    """
    def set_sweep_interval(self, iteration_interval):
        self.current_sweep_interval = iteration_interval
    
    """
    Move the joint to its destination in a loop. This function is meant to be called in a thread.
    """
    def move_to_destination(self):
        # Set moving flag
        self.is_moving = True
        # Start moving
        while True:
            # Check if the joint is already at its destination
            if self.current_angle == self.destination:
                # Notify
                print(f"Joint #{self.joint_num} is at destination {self.destination}.")
                # Clear moving flag
                self.is_moving = False
                # Finish the thread
                return
            # Check direction of movement
            if self.current_angle < self.destination:
                self.current_angle += 1
            else:
                self.current_angle -= 1
            self.servo.angle = self.current_angle
            # Wait for the next iteration
            time.sleep(self.current_sweep_interval)
    
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