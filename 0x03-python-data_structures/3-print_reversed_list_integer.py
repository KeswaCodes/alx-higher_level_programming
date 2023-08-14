#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = 0

    if my_list is None:
        return None
    else:
        for element in range(len(my_list), 0, -1):
            print("{}". format(my_list.pop(-1)))
            i += 1
