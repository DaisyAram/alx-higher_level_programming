#!/usr/bin/python3
class Square:
    def __init__(self, size):
        """
        initialize a new square.
        Args:
          size (int): size of new square
        """

        self.size = size

    @property
    def size(self):
        """
        get the current size of the square.
        Args:
         self(square): square instance
        Returns:
         (int): current size of the square
         """

        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Return the current area of the square.
        Args:
         self(square): square instance.
        Returns:
         (int): current area of square.
         """

        return self._size * self._size

    def my_print(self):
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
