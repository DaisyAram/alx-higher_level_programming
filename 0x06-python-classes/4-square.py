#!/usr/bin/python3
"""def Square module."""


class Square:

    """Represents a square."""

    def __init__(self, size=0):

        """Initialiaze a new square.

        Args:

            size(int): size of the square.

        """
        self.size = size

        @property
        def size(self):
            """Get/set the current size of square."""

            return (self.__size)

        @size.setter
        def size(self, value):
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")

            def area(self):
                """Return the current area of the square."""
                return (self._size * self._size)
