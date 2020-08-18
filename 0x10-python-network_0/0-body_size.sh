#!/bin/bash
# script that sends a request to a url                                  
curl -sI "$1" | grep "Content-Lenght:" | cut -f2 -d ' '
