#!/usr/bin/python3
"""module defines a square"""


class Square:
    """
    Class defines a square
    Attributes
    size (int): the length of one side of a square
    """
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

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

    def my_print(self):
        """prints the square"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                if self.position[0] > 0:
                    print(" " * self.__position[0], end='')
                print("#" * self.__size)

    @property
    def position(self):
        """getter retrieves co-ordinates of square"""
        return self.__position

    @position.setter
    def position(self, value):
        """setter method that alters position atribute"""

        if not (isinstance(value, tuple) and len(value) != 2 and value > 0):
            raise TypeError("position must be a tuple of 2 integers")
