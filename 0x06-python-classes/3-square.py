#!/usr/bin/python3
"""module defines a square"""


class Square:
    """
    Class defines a square

    Attributes
    size (int): the length of one side of a square
    """
    def __init__(self, size=0):
        """initializes the object"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

        else:
            self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size * self.__size
