#!/bin/bash
# script that sends a POST request
curl -X POST -sd "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
