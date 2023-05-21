from flask import Flask
from sixdof_arm import Robot
import os

app = Flask(__name__)
robot = Robot()

@app.route('/')
def display_welcome_message():
    return "<p>You have found the 6 DoF robot backend server!</p><p>Use the client app to interact with this server meaningfully.<p>"

"""
This endpoint is used to move the robot arm to a target angles of each joint.
:param target_dict: A JSON containing the target angles for each joint.
:return: Success or failure message.
"""
@app.route('/target_angles', methods=['POST'])
def move_to():
    pass

"""
Route and helper function to show version number of system.
Open the version.txt file and return the contents. If it doesn't exist, notify, show current directory and exit.
"""
@app.route('/version')
def show_version():
    try:
        with open('version.txt') as f:
            version = f.read()
    except FileNotFoundError:
        print("version.txt not found in current directory.")
        print("Current directory is:")
        print(os.getcwd())
        exit()
    return version

if __name__ == "__main__":
    # Show the version number of the system
    print(show_version())
    # Run the Flask app
    app.run(host='0.0.0.0')