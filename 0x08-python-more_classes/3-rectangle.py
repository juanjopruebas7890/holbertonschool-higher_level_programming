#!/usr/bin/python3
""" Creating a rectangle """


class Rectangle:
    """ define class """
    def __init__(self, width=0, height=0):
        """ inititialize variables """
        self.width = width
        self.height = height

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
        st += ('#' * self.__width + '\n') * self.__height
        return (st[:-1])
