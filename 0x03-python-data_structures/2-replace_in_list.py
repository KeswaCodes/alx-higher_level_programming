#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    if idx is None or idx >= len(my_list):
        return my_list
    else:
        if element is None:
            return my_list
        else:
            del my_list[idx]
            my_list.insert(idx, element)
            return my_list
