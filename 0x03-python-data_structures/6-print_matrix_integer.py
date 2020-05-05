#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for a in range(len(matrix)):
        for l in range(len(matrix[a])):
            if l == len(matrix[l]) - 1:
                print("{:d}".format(matrix[a][l]), end='')
            else:
                print("{:d}".format(matrix[a][l]), end=' ')
        print()
