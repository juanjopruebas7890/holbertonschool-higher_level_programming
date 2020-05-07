#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    t = []
    for i in matrix:
        t.append(list(map(lambda r: r ** 2, i)))
    return (t)
