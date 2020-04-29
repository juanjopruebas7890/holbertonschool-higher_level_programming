#!/usr/bin/python3
def uppercase(str):
    for l in range(len(str)):
        z = ord(str[l])
        if z >= 97 and z <= 123:
            z -= 32
        print("{}".format(chr(z)), end="")
    print()
