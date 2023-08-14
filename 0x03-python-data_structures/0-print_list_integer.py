#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    else:
        for element in range(1, len(my_list) + 1):
            print("{:d}".format(element))
