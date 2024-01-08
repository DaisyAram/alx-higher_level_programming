#!/usr/bin/python3
def add_attribute(obj, att, value):
    """Add a new attribute to an object if possible.

    Args:
        obj (any): The object to add an attribute to.
        att (str): The name of the attribute to add to obj.
        value (any): The value of att.
    Raises:
        TypeError: If the attribute cannot be added.
    """
    # Check if the object can have new attributes
    if isinstance(obj, (type, int, float, bool, bytes, str, tuple, set, frozenset)):
        raise TypeError("can't add new attribute")

    # Add the new attribute to the object
    setattr(obj, att, value)
