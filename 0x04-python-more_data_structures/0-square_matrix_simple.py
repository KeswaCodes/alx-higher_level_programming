#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    if len(matrix) == 0:
        return None

    my_matrix = []
    my_list = []
    for list in matrix:

        for element in list:

            my_list.append(element ** 2)
        my_matrix.append(my_list)
        my_list = []

    return my_matrix
