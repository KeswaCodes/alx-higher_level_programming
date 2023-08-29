#!/usr/bin/python3
"""This module defines a class for square"""


class Square:
    """
    Class for a square
    Attributes:
    __size (int): the lenght of one side of a square
    """
    def __init__(self, __size=None):
        """ initializes object """
        self.__size = __size
