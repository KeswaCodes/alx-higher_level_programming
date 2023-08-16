#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    if a_dictionary is None:
        return None

    my_dictionary = {}
    for key in a_dictionary:
        value = a_dictionary.get(key)
        value = value * 2
        my_dictionary[key] = value

    return my_dictionary
