#!/usr/bin/python3
"""
This module contains the function say_my_name()
"""
def say_my_name(first_name, last_name=""):

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
   
    if first_name and last_name:
        print("My name is {} {}".format(first_name, last_name))
    elif first_name:
        print("My name is {}". format(first_name))
    else:
        print("My name is")
