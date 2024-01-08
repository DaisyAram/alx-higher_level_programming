#!/usr/bin/python3
"""defines class BaseGeometry"""


class BaseGeometry:
    """represents basegeometry"""

    def area(self):
        """raises exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer."""

        if type(value) != int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """represents basegeometry"""

    def __init__(self, width, height):
        """instantation of a rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """informal string rep of the rectangle"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)
