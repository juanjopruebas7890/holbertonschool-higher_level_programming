#!/bin/bash
# script that sends a POST request
curl -so /dev/null -w "%{http_code}" "$1"
