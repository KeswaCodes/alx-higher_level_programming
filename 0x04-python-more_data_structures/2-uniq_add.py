#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list is None:
        return None

    number_list = []
    result = 0

    for element in my_list:
        if element in number_list:
            continue
        number_list.append(element)
        result += element

    return result
