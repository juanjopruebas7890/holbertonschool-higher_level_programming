#!/usr/bin/python3
""" returns an object in python """


import json


def from_json_string(my_str):
    """ will return an obj """
    return (json.loads(my_str))
