#!/usr/bin/python3
""" Create a Square """


class Square:
    """ Define class

     Attributes:
    __size: size of the square
    """
    def __init__(self, size=0):
        """ Square initialized
        
        Arguments:
          size: size of the sqr
        return: None
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
            else:
                raise TypeError("size must be an integer")

    def area(self):
        """ Multiplication to find area
          return: area
        """
        return (self.__size * self.__size)
