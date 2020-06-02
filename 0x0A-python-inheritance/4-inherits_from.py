#!/usr/bin/python3
""" tells if the object is an instance that was inherited """


def inherits_from(obj, a_class):
    """ return if is inherited """
    if (type(obj) != a_class):
        return (isinstance(obj, a_class))
    else:
        return (False)
