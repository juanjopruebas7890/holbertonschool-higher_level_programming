#!/usr/bin/python3
def max_integer(my_list=[]):
    m = my_list[0]
    for i in my_list:
        if i == 0:
            return (None)
        elif i > m:
            m = i
    return (m)
