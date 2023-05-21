#!/bin/sh

# This function takes in filename as an argument, and gets it via scp from the RPi
get_file_from_pi() {
    scp pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/$1 ./$1
}

get_dir_from_pi() {
    scp -r pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/$1 .
}

# Get files from the pi
get_file_from_pi joint-tester.py
get_file_from_pi robot-properties.json
get_dir_from_pi server
get_dir_from_pi sixdof_arm