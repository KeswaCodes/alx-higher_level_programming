#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return None

    if len(key.strip()) == 0:
        return None

    if value is None:
        return None

    a_dictionary[key] = value

    return a_dictionary
