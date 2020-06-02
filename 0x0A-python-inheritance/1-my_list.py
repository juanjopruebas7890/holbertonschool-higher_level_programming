#!/usr/bin/python3
""" create a class """


class MyList(list):
    """ class will inheri from a list """

    def print_sorted(self):
        """ wil, print the list """
        print(sorted(self))
