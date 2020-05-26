#!/usr/bin/python3
""" Creating a rectangle """


class Rectangle:
    """ define class """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """ inititialize variables """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ will get the widith
        return: the widith
        """
        return (self.__width)

    @property
    def height(self):
        """ will get the height
        return: the height
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        """ setter of the size """
        if type(value) is int:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, value):
        """ setter of height """
        if type(value) is int:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value
        else:
            raise TypeError("height must be an integer")

    def area(self):
        """ method to find area """
        return (self.__height * self.__width)

    def perimeter(self):
        """ method to find perm """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__height + self.__width + self.__width)

    def __str__(self):
        """ print # """
        st = ''
        if self.__width == 0 or self.__height == 0:
            return st
        st += ((str(self.print_symbol) * self.__width + '\n') * self.__height)
        return (st[:-1])

    def __repr__(self):
        """ return str representation of rect """
        return ("Rectangle({:d}, {:d})".format(self.__width, self.__height))

    def __del__(self):
        """ will check if something is deleted """
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')
