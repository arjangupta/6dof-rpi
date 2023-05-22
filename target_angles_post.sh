#!/bin/sh

# Use curl to POST the JSON string to the RPi
curl http://raspberrypitwo.local:5000/target_angles \
    -X POST -H "Content-Type: application/json" \
    -d '{"joint1": '$1', "joint2": '$2', "joint3": '$3', "joint4": '$4', "joint5": '$5', "joint6": '$6'}'
