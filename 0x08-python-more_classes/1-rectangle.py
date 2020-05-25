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
    def height(self, value):
        """ will get the height
        return: the height
        """
        return (self.__height)

    @width.setter
    def width(self, value):
        """ setter of width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """ setter of height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
