#!/usr/bin/python3
"""def Square module."""


class Square:

    """Represents a square."""

    def __init__(self, size=0):

        """Initialiaze a new square.

        Args:

            size(int): size of the square.

        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
