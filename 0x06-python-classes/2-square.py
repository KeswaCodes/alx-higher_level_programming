#!/usr/bin/python3
"""This module defines a class for square"""


class Square:
    """
    Class for a square
    Attributes:
    __size (int): the lenght of one side of a square
    """
    def __init__(self, size=0):
        """ initializes object """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
