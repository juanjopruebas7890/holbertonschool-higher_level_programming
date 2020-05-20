#!/usr/bin/python3
""" Create a square """


class Square:
    """ Define class

    Attributes:
    __size: Size of the square
    """
    def __init__(self, size=0):
        """ square initialized

        Arguments:
        size = size of sqr
        return: None
        """
        self.__size = size

        @property
        def size(self):
            """ Will get the size

            return: Size of sqr
            """
            return (self.__size)

        @size.setter
        def size(self, value):
            """ setter of __size

            s = size of sqr
            """
            if type(value) is int:
                if value < 0:
                    raise ValueError("size must be >= 0")
                else:
                    self.__sie = value
            else:
                raise TypeError("size must be an integer")

        def area(self):
            """ Multiplication to find area

            return: area of sqr
            """
            return (self.__size * self.__size)
