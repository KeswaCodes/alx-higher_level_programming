#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):

    if len(tuple_a) < 2:
        if len(tuple_a) == 1:
            tuple_a_first_int = tuple_a[0]
            tuple_a = (tuple_a_first_int, 0)
        elif len(tuple_b) == 0:
            tuple_a = (0, 0)

    elif len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b_first_int = tuple_b[0]
            tuple_b = (tuple_b_first_int, 0)
        elif len(tuple_b) == 0:
            tuple_b = (0, 0)

    first_element = tuple_a[0] + tuple_b[0]
    second_element = tuple_a[1] + tuple_b[1]
    my_tuple = (first_element, second_element)

    return my_tuple
