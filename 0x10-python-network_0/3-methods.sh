#!/bin/bash
# script that sends a request to a url
curl -sI "$1" | grep "Allow:" | cut -f 2 -d' '
