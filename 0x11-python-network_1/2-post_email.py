#!/usr/bin/python3
""" takes in a url and sends a POST request """


import sys
from urllib import request, parse


if __name__ == '__main__':
    url = sys.argv[1]
    mail = {'email': sys.argv[2]}

    data = parse.urlencode(mail)
    data = data.encode('ascii')
    req = request.Request(url, data)
    with request.urlopen(req) as response:
        resp = response.read()
        print(resp.decode('utf-8'))
