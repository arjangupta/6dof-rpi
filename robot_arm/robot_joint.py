"""
This file defines the RobotJoint class, which is used to control a single joint of the robot arm.
"""

from adafruit_motor import servo

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
        self.current_destination = self.current_angle
        self.current_sweep_interval = 0.02
    
    """
    Sets a destination angle for the joint to move to.
    :param angle: The destination angle for the joint to move to.
    """
    def set_destination(self, angle):
        # Check if the angle is within the range of motion of the joint
        if angle < 0 or angle > self.angle_range:
            print(f"Angle of {angle} given to joint #{self.joint_num} is out of range.")
            return
        self.current_destination = angle
    
    """
    Set an angular speed as a sweep interval for the joint to move to its destination.
    :param iteration_interval: The time interval between each iteration of the sweep.
    """
    def set_sweep_interval(self, iteration_interval):
        self.current_sweep_interval = iteration_interval
    
    """
    Move the joint to its destination.
    """
    def move_to_destination(self):
        # Check if the joint is already at its destination
        if self.current_angle == self.current_destination:
            # Notify
            print(f"Joint #{self.joint_num} is already at its destination.")
            return
        # Check direction of movement
        if self.current_angle < self.current_destination:
            self.current_angle += 1
        else:
            self.current_angle -= 1
        self.servo.angle = self.current_angle
        

