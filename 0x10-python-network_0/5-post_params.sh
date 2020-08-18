#!/bin/bash
# script that sends a POST request
curl -X POST -sd "email=hr@holbertonschool.com&subject=I will always be here fo\
r PLD" "$1"
