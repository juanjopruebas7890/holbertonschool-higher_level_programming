#!/usr/bin/python3
""" class that inherits """
BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ class that inherits """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
    """ return area """
    def area(self):
        return (self.__width * self.__height)
    """ return size """
    def __str__(self):
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))
