#!/usr/bin/python3
"""
divide all elements in a matrix
"""


def matrix_divided(matrix, div):
    """
    Arguments:

    Matrix: list of int or floats

    div: need to be a number

    """
    if type(matrix) is not list:
        raise TypeError("matrix must be a matrix" +
                        "(list of lists) of integers/floats")

    rw = 0
    for p in matrix:
        for t in p:
            if type(t) not in [int, float]:
                raise TypeError("matrix must be a matrix" +
                                "(list of lists) of integers/floats")

    if rw == 0:
        rw = len(p)
    elif rw != len(p):
        raise TypeError("matrix must be a matrix" +
                        "(list of lists) of integers/floats")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(t / div, 2) for t in p] for p in matrix]
