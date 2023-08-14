#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        for element in range(1, len(my_list) + 1):
            print("{:d}".format(element))
