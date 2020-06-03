#!/usr/bin/python3
""" reads n lines of a text """


def read_lines(filename="", nb_lines=0):
    """ read lines """
    with open("my_file_0.txt", encoding="utf-8") as file:
        if nb_lines <= 0:
            for line in file:
                print(line)
        else:
            for line in range(nb_lines):
                print(file.readline(), end="")
