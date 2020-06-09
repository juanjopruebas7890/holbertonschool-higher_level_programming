#!/usr/bin/python3
""" create class square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ will define a square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Attributes """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ size getter """
        return (self.width)

    @size.setter
    def size(self, value):
        """ setter for size """
        self.width = value
        self.height = value

    def __str__(self):
        """ print """
        return ("[Square] ({}) {}/{} - {}".format(self.id, self.x,
                                                  self.y, self.width))

    def update(self, *args, **kwargs):
        """ assign attributes """
        if len(args) > 0:
            for i in range(len(args)):
                if i == 0:
                    self.id = args[0]
                if i == 1:
                    self.width = args[1]
                    self.height = args[1]
                if i == 2:
                    self.x = args[2]
                if i == 3:
                    self.y = args[3]
        else:
            if len(kwargs) > 0:
                for i in kwargs.keys():
                    if i == "id":
                        self.id = kwargs["id"]
                    if i == "size":
                        self.width = kwargs["size"]
                        self.height = kwargs["size"]
                    if i == "x":
                        self.x = kwargs["x"]
                    if i == "y":
                        self.y = kwargs["y"]

    def to_dictionary(self):
        """ dicionary """
        sd = {"id": self.id, "size": self.size, "x": self.x, "y": self.y}
        return (sd)
