#!/usr/bin/python3
""" will create an object """


import json


def load_from_json_file(filename):
    """ create an obj from json """
    with open(filename, mode="r", encoding="utf-8") as file:
        return (json.loads(file.read()))
