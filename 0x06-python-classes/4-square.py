#!/usr/bin/python3
"""module defines a square"""


class Square:
    """
    Class defines a square
    Attributes
    size (int): the length of one side of a square
    """
    def __init__(self, size=0):
        self.__size = size

    def area(self):
        """returns the area of a square"""
        return self.__size * self.__size

    @property
    def size(self):
        """getter method to retrieve the value of size"""
        return self.__size

    @size.setter
    def size(self, value):
        """setter method sets value"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
