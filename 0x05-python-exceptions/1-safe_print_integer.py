#!/usr/bin/python3
def safe_print_integer(value):
    while value == int:
        try:
            print("{:d}".format(value))
        except:
            break
