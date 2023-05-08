#!/bin/sh

# Use scp to copy the file to the pi
scp ./controller.py pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/controller.py
scp ./version.txt   pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/version.txt