#!/usr/bin/python3
"""function contains module is_same_class"""


def is_same_class(obj, a_class):
    """returns True if the obj is exactly
    an instance of the specified class ; otherwise False."""
    return (type(obj) == a_class)
