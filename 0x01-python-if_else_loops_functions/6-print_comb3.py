#!/usr/bin/python3
for l in range(0, 9):
    for z in range(l + 1, 10):
        if (l < 8):
            print("{}{}".format(l, z), end=", ")
        else:
            print("{}{}".format(l, z))
