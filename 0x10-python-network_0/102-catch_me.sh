#!/bin/bash
# script that sends a POST request
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" 0.0.0.0:5000/catch_me
