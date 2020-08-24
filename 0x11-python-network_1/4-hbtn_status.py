#!/usr/bin/python3
""" fetches a url with requests package """


import requests

if __name__ == '__main__':
    r = requests.get('https://intranet.hbtn.io/status', auth=('user', 'pass'))
    print('Body response:')
    print('\t- type: {}'.format(type(r.text)))
    print('\t- content: {}'.format(r.text))
