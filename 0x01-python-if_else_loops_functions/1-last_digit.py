#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
d = 10
l = number % d
# YOUR CODE HERE
if (l > 5):
    print("Last digit of", number, "is", l, "and is greater than 5")
elif(l == 0):
    print("Last digit of", number, "is", l, "and is 0")
elif(l < 6):
    print("Last digit of", number, "is", l, "and is less than 6 and not 0")
