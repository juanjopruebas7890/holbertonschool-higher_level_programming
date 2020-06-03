#!/usr/bin/python3
""" writes an object to a text file """


import json


def save_to_json_file(my_obj, filename):
    """ will write an object """
    with open(filename, mode="w") as file:
        return (json.dumps(my_obj, file))
