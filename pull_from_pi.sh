#!/bin/sh

# Get files from the pi
scp pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/controller.py   ./controller.py
scp pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/version.txt     ./version.txt
scp pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/range-tester.py ./range-tester.py