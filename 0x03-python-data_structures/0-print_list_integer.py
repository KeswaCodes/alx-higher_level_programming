#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if my_list is None or len(my_list) == 0:
        return None
    else:
        for element in my_list:
            print("{:d}".format(element))
