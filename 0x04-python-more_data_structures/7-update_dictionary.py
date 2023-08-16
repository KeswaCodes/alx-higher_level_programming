#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    if a_dictionary is None:
        return None

    key = key.strip()
    if len(key) == 0:
        return None

    if value is None or len(value.strip()) == 0:
        return None

    a_dictionary[key] = value

    return a_dictionary
