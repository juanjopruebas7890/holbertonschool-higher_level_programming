#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    
    if (len(argv) - 1 == 0):
        print(0)
    elif (len(argv) - 1 >= 1):
        r = 0
        for p in range(1, len(argv)):
            r += int(argv[p])
        print(r)
