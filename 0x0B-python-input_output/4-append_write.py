#!/usr/bin/python3
""" will append a stringat the end of a file """


def append_write(filename="", text=""):
    """ return an appended string """
    with open(filename, mode="a") as file:
        return (file.write(text))
