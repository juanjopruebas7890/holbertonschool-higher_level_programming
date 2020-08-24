#!/usr/bin/python3
""" takes a url and sends request with requests package """

import requests
import sys

if __name__ == '__main__':
    url = 'http://0.0.0.0:5000/search_user'
    var = {'q': ''}

    try:
        var['q'] = sys.argv[1]
    except:
        pass

    r = requests.post(url, var)

    try:
        js = r.json()
        if js:
            print("[{}] {}".format(js["id"], js["name"]))
        else:
            print("No result")

    except:
        print("Not a valid JSON")
