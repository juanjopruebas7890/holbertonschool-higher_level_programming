#!/usr/bin/python3
""" takes in a url and handles an error """


import sys
from urllib import request, parse, error


if __name__ == '__main__':
    try:
        with request.urlopen(sys.argv[1]) as response:
            resp = response.read()
            print(resp.decode('utf-8'))
    except error.HTTPError as error:
        print("Error code: {}".format(error.code))
