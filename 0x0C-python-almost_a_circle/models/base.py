#!/usr/bin/python3
""" Base class """


import json
import os


class Base:
    """ define class """

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ json to string """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ json string representation """
        object_list = []
        if object_list is None or len(list_objs) == 0:
            object_list = []
        else:
            for t in list_objs:
                object_list.append(t.to_dictionary())
        with open("{}.json".format(cls.__name__), mode="w",
                  encoding="utf-8") as file:
            file.write(Base.to_json_string(object_list))

    @staticmethod
    def from_json_string(json_string):
        """ return list of json string """
        if json_string is None or json_string == 0:
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with attributes """
        if cls.__name__ == "Rectangle":
            tmp = cls(1, 1)
        if cls.__name__ == "Square":
            tmp = cls(1)
        tmp.update(**dictionary)
        return (tmp)

    @classmethod
    def load_from_file(cls):
        """ return list of istances """
        fl = "{}.json".format(cls.__name__)

        try:
            with open(fl, encoding="utf-8") as file:
                p = file.read()
                d_inst = cls.from_json_string(p)
                i_inst = []
                for i in d_inst:
                    i_inst.append(cls.create(**i))
                return (i_inst)
        except IOError:
            return ([])
