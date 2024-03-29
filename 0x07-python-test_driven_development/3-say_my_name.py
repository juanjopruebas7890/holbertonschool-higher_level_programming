#!/usr/bin/python3
""" print names
"""


def say_my_name(first_name, last_name=""):
    """
    Arguments:

    First_name: first name

    last_name: last name

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if isinstance(first_name, str) and isinstance(last_name, str):
        print("My name is {} {}".format(first_name, last_name))
