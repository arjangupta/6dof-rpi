#!/bin/sh

curl http://raspberrypitwo.local:5000/target_angles \
    -X POST -H "Content-Type: application/json" \
    -d '{"joint1": 90, "joint2": 90, "joint3": 90}'
