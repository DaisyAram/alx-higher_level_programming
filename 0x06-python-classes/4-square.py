#!/usr/bin/python3
"""Represent a square."""


class Square:
    """Represent a square"""

    def __init__(self, size=0):
        """initialize a new square.

        Args:

        size (int): The size of new square.

        """

        self.size = size

    @property
    def size(self):
        """Get current size of square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return current area of square."""
        return (self.__size ** 2)
