#!/usr/bin/python3
"""contains class BaseGeometry and subclass Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """represents ba square"""

    def __init__(self, size):
        """instantation of a square"""

        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """returns area"""
        return self.__size ** 2
