#!/usr/bin/python3
"""
This module contains only one function
FUNCTION
add_integer(a, b) : adds two integers
"""
def add_integer(a, b=98):
    """
    this function adds two integers together
    """

    if isinstance(a, (int, float)):
        a = int(a)
    else:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)):
        b = int(b)
    else:
        raise TypeError("b must be an integer")
        
    return a + b
