#!/usr/bin/python3
"""defines a rectangle"""


class Rectangle:
    """ rep a rectangle"""
    def __init__(self, length=0, width=0):
        """ init a new rectangle
        args:
        width(int): width of a rectangle
        length(int): length of a rectangle
        """
        self.length = length
        self.width = width

        @property
        def width(self):
            """Get/set the width of the rectangle."""
            return self.__width

        @width.setter
        def width(self, value):
            if not isinstance(value, int):
                raise TypeError("width must be an integer")
            if value < 0:
                raise ValueError("width must be >= 0")
            self.__width = value

        @property
        def height(self):
            """Get/set the height of the rectangle."""
            return self.__height

        @height.setter
        def height(self, value):
            if not isinstance(value, int):
                raise TypeError("height must be an integer")
            if value < 0:
                raise ValueError("height must be >= 0")
            self.__height = value
