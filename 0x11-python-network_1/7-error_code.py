#!/usr/bin/python3
""" takes a url and sends request with requests package """

import requests
import sys

if __name__ == '__main__':
    code = requests.get(sys.argv[1])

    if code.status_code < 400:
        print(code.text)
    else:
        print("Error code: {}".format(code.status_code))
