#!/usr/bin/python3
"""Documentation for rectangle class"""


from models.base import Base


class Rectangle(Base):
    """Rectangle class which inherits from Base class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """ attributes """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ getter for width """
        return (self.__width)

    @width.setter
    def width(self, value):
        """ width setter """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ getter of height """
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter for height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ getter for x """
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter for x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ getter for y """
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter for y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area """
        return (self.width * self.height)

    def display(self):
        """ displays # """
        if self.width == 0 or self.height == 0:
            return
        for i in range(self.y):
            print()
        for t in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """ printing method """
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.x, self.y, self.width, self.height))

    def update(self, *args, **kwargs):
        """ assign attribute """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                if i == 2:
                    self.height = args[2]
                if i == 3:
                    self.x = args[3]
                if i == 4:
                    self.y = args[4]
        else:
            if len(kwargs) > 0:
                for i in kwargs.keys():
                    if i == "id":
                        self.id = kwargs["id"]
                    if i == "width":
                        self.width = kwargs["width"]
                    if i == "height":
                        self.height = kwargs["height"]
                    if i == "x":
                        self.x = kwargs["x"]
                    if i == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """ dictionary """
        recd = {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
        return (recd)
