#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    if len(a_dictionary) == 0:
        return None

    sorted_list = sorted(a_dictionary)

    for key in sorted_list:
        value = a_dictionary.get(key)
        sentence = key + ": " + str(value)
        print(sentence)
