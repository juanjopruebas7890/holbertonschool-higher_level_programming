#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    nd = dict(a_dictionary)
    for key in a_dictionary:
        nd[key] = a_dictionary[key] * 2
    return (nd)
