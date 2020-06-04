#!/usr/bin/python3
""" define a student """


class Student:
    """ define class """
    def __init__(self, first_name, last_name, age):
        """ initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves a dict """
        if attrs is None:
            return (self.__dict__)
        dic = {}
        for attribute in attrs:
            try:
                dic[attribute] = self.__dict__[attribute]
            except:
                pass
        return (dic)

    def reload_from_json(self, json):
        """ replaces attrbutes student """
        for key in json:
            try:
                setattr(self, key, json[key])
            except:
                pass
