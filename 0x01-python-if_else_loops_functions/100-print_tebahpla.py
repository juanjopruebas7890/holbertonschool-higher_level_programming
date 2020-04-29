#!/usr/bin/python3
for l in range(122, 96, -1):
    if (l % 2 == 0):
        print("{}".format(chr(l)), end="")
    else:
        print("{}".format(chr(l - 32)), end="")
