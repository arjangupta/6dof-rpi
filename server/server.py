from flask import Flask
from sixdof_arm import Robot

PROJECT_VERSION = "0.0.6"

app = Flask(__name__)
robot = Robot()

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
    pass

@app.route('/version')
def show_version():
    return f"<p>Overall project version is {PROJECT_VERSION}.</p>"

if __name__ == "__main__":
    # Run the Flask app
    app.run()