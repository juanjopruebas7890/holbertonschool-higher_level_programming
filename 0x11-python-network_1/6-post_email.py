#!/usr/bin/python3
""" takes a url and sends a POSTS request with requests package """

import requests
import sys

if __name__ == '__main__':
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}

    r = requests.post(url, mail)
    print("Your email is: {}".format(sys.argv[2]))
