#!/usr/bin/python3
def print_last_digit(number):
    if (number < 0):
        l = (number * -1)
        print("{}".format(l % 10) * 2)    
    else:
        print("{}".format(number % 10), end="")
