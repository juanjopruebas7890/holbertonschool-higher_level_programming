#!/usr/bin/python3
""" Define class square """


class Square:
    """ Define class
    Attributes:
    __size: size of the square
    """
    def __init__(self, size=0):
        """ Square initialized
        Arguments:
        size: size fo the sqr
        return: none
        """
        self.__size = size

    @property
    def size(self):
        """ will get the size
        return: size of sqr
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter of size
        s = size os sqr
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    def area(self):
        """ method to find area
        return: area of sqr
        """
        return (self.__size * self.__size)
