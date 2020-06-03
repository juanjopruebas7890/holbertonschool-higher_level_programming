#!/usr/bin/python3
""" returns number of lines """


def number_of_lines(filename=""):
    """ will give number of lines """
    count = 0
    with open(filename, mode="r", encoding="utf-8") as file:
        for line in file:
            count += 1
        return (count)
