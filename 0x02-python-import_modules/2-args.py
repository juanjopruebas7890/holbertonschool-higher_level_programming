#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    if (len(argv) - 1 == 0):
        print("0 arguments.")
    elif (len(argv) - 1 == 1):
        print("{} argument:".format(len(argv) - 1))
        print("{}: {}".format(len(argv) - 1, argv[1]))
    elif (len(argv) - 1 >= 2):
        print("{:d} arguments:".format(len(argv) - 1))
        for p in range(1, len(argv)):
            print("{:d}: {}".format(p, argv[p]))
