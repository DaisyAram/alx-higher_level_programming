#!/usr/bin/python3
"""func to add integers"""


def add_integer(a, b=98):
    """
    function to add 2 integers or floats.
    Args:
        a (int, float): The first number.
        b (int, float, optional): The second number, default is 98.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # Convert a and b to integers if they are floats
    a = int(a)
    b = int(b)
    return (a + b)
