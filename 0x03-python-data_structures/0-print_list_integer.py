#!/usr/bin/python3
def print_list_integer(my_list=[]):
    if not my_list:
        return
    else:
        print("{}".format(my_list[:]))
