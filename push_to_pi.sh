#!/bin/sh

# This function takes in filename as an argument, and pushes it via scp to the RPi
push_file_to_pi() {
    scp ./$1 pi@$rpi2:~/workspace/6dof-rpi-deployment/$1
}

push_dir_to_pi() {
    scp -r ./$1 pi@$rpi2:~/workspace/6dof-rpi-deployment/
}

# Use scp to copy the file to the pi
push_file_to_pi robot-properties.json
push_dir_to_pi sixdof_arm
push_dir_to_pi server
# push_dir_to_pi joint_tester