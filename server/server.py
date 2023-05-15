from flask import Flask

app = Flask(__name__)

@app.route('/')
def display_welcome_message():
    return "<p>You have found the 6 DoF robot backend server!</p><p>Use the client app to interact with this server meaningfully.<p>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')