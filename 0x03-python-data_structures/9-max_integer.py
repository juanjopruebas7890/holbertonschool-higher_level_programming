#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return (None)
    n = my_list[:]
    n.sort()
    return (n[-1])
