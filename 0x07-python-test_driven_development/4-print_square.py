#!/usr/bin/python3
"""
prints a square
"""


def print_square(size):
    """
    size: Variable

    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for l in range(size):
        for a in range(size):
            print("#", end="")
        print("")
