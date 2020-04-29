#!/usr/bin/python3
def remove_char_at(str, n):
    l = ""
    z = 0
    for q in str:
        if z != n:
            l = l + q
        z = z + 1
    return (l)
