#!/bin/sh

# This function takes in filename as an argument, and pushes it via scp to the RPi
push_file_to_pi() {
    scp ./$1 pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/$1
}

# Use scp to copy the file to the pi
push_file_to_pi version.txt
push_file_to_pi joint-tester.py
push_file_to_pi robot-properties.json