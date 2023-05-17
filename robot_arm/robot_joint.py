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
    Set an angular speed setting (levels 1-5) for the joint to move at.
    :param speed: The angular speed for the joint to move at.
    """
    def set_angular_speed(self, speed):
        # Check if speed is within the range of 1-5
        if speed < 1 or speed > 5:
            print(f"Speed setting of {speed} given to joint #{self.joint_num} is out of range.")
            return
        # Set the sweep interval based on the speed setting
        self.current_sweep_interval = 0.01 * speed
        

