#!/usr/bin/python3
""" writes a string and returns the # of char """


def write_file(filename="", text=""):
    """ returns # of char """
    with open(filename, mode="w", encoding="utf-8") as file:
        return (file.write(text))
