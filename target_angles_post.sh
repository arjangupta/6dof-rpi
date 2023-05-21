#!/bin/sh

curl http://raspberrypitwo.local:5000/target_angles -X POST -H "Content-Type: application/json" -d '{"target_dict": "Hello"}'
