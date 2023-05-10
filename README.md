# 6 DoF Robotic Arm Controlled by Raspberry Pi

This is my personal project. So far the hardware consists of:

- Raspberry Pi 2B
- PCA9685 hat for the Pi
- Robotic arm with six MG996R servos
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
