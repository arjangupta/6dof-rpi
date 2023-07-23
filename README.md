# 6 DoF Robotic Arm Controlled by Raspberry Pi

This is my personal project. So far the hardware consists of:

- Raspberry Pi 2B
- PCA9685 hat for the Pi
- Robotic arm (diymore ROT3Us) with six MG996R servos
- Separate power supplies for the Pi and the servos

## Dependencies on RPi

```sh
sudo apt-get install python-smbus
sudo apt-get install i2c-tools # might already get installed with the above
```

After that, detect the 0x40 address of the PCA9685 hat:

```sh
sudo i2cdetect -y 1
```

For the Adafruit library, execute the following:

```sh 
pip3 install adafruit-circuitpython-servokit
```

## Development dependencies for Flask server

```sh
pip3 install flask
```

You might also need to install the following:

```sh
pip3 install typeguard
```

Then, do the following:

```sh
export FLASK_APP=server/server.py
flask run
```

You will now see the server running. By opening localhost:5000, you can see a reply from the server.

## Visualization of URDF

The kinematics/sixdof_arm.urdf file can be visualized in Foxglove Studio. To do that, install Foxglove Studio and open the file in it under "Custom layers".
