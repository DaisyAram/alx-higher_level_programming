#!/usr/bin/python3
"""contains class BaseGeometry and subclass Rectangle"""


BaseGeometry =  __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """represents a rectangle using basegeometry"""

    def __init__(self, width, height):
        """initialize a new rectangle"""

        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
