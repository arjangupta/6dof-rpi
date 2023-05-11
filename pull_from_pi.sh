#!/bin/sh

# This function takes in filename as an argument, and gets it via scp from the RPi
function get_file_from_pi() {
    scp pi@raspberrypitwo.local:~/workspace/6dof-rpi-deployment/$1 ./$1

# Get files from the pi
get_file_from_pi version.txt
get_file_from_pi joint-tester.py