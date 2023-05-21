from flask import Flask
from sixdof_robot import Robot

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(host='0.0.0.0')