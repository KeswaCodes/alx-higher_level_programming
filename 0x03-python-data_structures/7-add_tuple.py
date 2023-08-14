#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    my_tuple_a = ()
    my_tuple_a = tuple_a[:]
    my_tuple_b = ()

    if len(tuple_b) < 2:
        if len(tuple_b) == 1:
            tuple_b_first_int = tuple_b[0]
            my_tuple_b = (tuple_b_first_int, 0)
        elif len(tuple_b) == 0:
            my_tuple_b = (0, 0)

        else:
            pass

    else:
        my_tuple_b = tuple_b[:]

    first_element = my_tuple_a[0] + my_tuple_b[0]
    second_element = my_tuple_a[1] + my_tuple_b[1]
    my_tuple = (first_element, second_element)

    return my_tuple
