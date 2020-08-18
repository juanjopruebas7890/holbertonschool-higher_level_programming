#!/bin/bash
# script that sends a POST request
curl -sH "Content-Type: application/json" -d @"$2" "$1"
