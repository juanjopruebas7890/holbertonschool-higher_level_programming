#!/usr/bin/python3
""" Define a class square """


class Square:
    """ Define class

    Attributes:
    __size: size of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """ square initialized

        Arguments:
        size: size of the sqr
        return: none
        """

        self.size = size
        self.position = position

    @property
    def size(self):
        """ will get the size

        return: size of sqr
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """ setter of size

        s = size of sqr
        """
        if type(value) is int:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value
        else:
            raise TypeError("size must be an integer")

    @property
    def position(self):
        """ get the pos """
        return (self.__position)

    @position.setter
    def position(self, value):
        """ setter pos """
        if type(value) is not tuple or len(value) != 2 or
        type(value[0])is not int or value[0] < 0 or
        type(value[1]) is not int or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ find area """
        return (self.__size * self.__size)

    def my_print(self):
        """ print """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        for c in range(self.__size):
            print("".join([" " for q in range(self.__position[0])]), end="")
            print("".join(["#" for e in range(self.__size)]))
