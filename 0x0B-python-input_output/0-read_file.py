#!/usr/bin/python3
""" function that reads a text file """


def read_file(filename=""):
    """ will read a file """
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
