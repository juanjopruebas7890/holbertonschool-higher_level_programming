#!/usr/bin/python3
def square_matrix_map(matrix=[]):
    return list(map(lambda i: list(map(lambda t: t ** 2, i)), matrix))
