from flask import Flask
from flask import request
from sixdof_arm import Robot
import logging

PROJECT_VERSION = "0.0.7"

# Initialize Flask app and logging
app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

# Initialize the robot
robot = Robot()

"""
This endpoint (the default endpoint) is used to display a welcome message.
"""
@app.route('/')
def display_welcome_message():
    return f"<p>You have found the 6 DoF robot backend server. Overall project version is {PROJECT_VERSION}.</p><p>Use the client app to interact with this server meaningfully.<p>"

"""
This endpoint is used to move the robot arm to a target angles of each joint.
:param target_dict: A JSON containing the target angles for each joint.
:return: Success or failure message.
"""
@app.route('/target_angles', methods=['POST'])
def move_to():
    # Parse the JSON
    target_dict = request.get_json()
    # Show the target angles
    app.logger.debug(f"Target angles: {target_dict}")
    # Move the robot arm
    # robot.move_to(target_dict)
    # Return a success message
    return "Robot arm moved successfully.\n"

"""
This endpoint is used to get the current angles of each joint.
:return: A JSON containing the current angles of each joint.
"""
@app.route('/current_angles', methods=['GET'])
def get_current_angles():
    # Get the current angles of each joint
    current_angles = robot.get_current_positions()
    # Convert the list to JSON
    current_angles_json = {"current_angles": current_angles}
    # Return the current angles
    return current_angles

@app.route('/version')
def show_version():
    return f"<p>Overall project version is {PROJECT_VERSION}.</p>"

if __name__ == "__main__":
    # Run the Flask app
    app.run()