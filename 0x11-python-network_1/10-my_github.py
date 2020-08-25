#!/usr/bin/python3
""" takes a url and sends request with requests package """

import sys
from requests import auth, get


if __name__ == '__main__':
    url = 'https://api.github.com/user'
    user = sys.argv[1]
    passwrd = sys.argv[2]
    r = get(url, auth=auth.HTTPBasicAuth(user, passwrd))
    print(r.json().get('id'))
