#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    if a_dictionary is None:
        return None

    if len(key.strip()) == 0:
        return None

    dic_check = a_dictionary.get(key, "0")
    if dic_check == "0":
        return a_dictionary

    del a_dictionary[key]

    return a_dictionary
