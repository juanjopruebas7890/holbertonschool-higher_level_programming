#!/usr/bin/python3
""" class that inherits """
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ square inherits from rectangle """
    def __init__(self, size):
        """ define a rectangle """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)
