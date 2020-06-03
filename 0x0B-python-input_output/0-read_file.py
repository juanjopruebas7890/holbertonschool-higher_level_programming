#!/usr/bin/python3
""" function that reads a text file """


def read_file(filename=""):
    """ will read a file """
    with open("my_file_0.txt", mode="r", encoding="utf-8") as file:
        for line in file:
            print(line, end="")
