#!/usr/bin/python3
"""
This module contains the function for matrix_divided()

matrix: list of lists
div: number to divide by
"""
def matrix_divided(matrix, div):
    if matrix is None:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    # create a list to check the length of each of the rows in the matrix
    len_list = []
    i = 0
    for row in matrix:
        # i variable keeps track of the number of rows
        i += 1
        len_list.append(len(row))
    # get the first length from the list of row lengths to see if the length of the rows are equal by checking the occurances
    x = len_list[0]
    check_rows_equal = len_list.count(x)

    # if the number of occurances does not match the number of times we ran the loop above, the length of the rows are not equal
    if not check_rows_equal == i:
        raise TypeError("Each row of the matrix must have the same size")
    
    my_matrix = []
    for row in matrix:
        new_list = []
        for element in row:
            if not isinstance(element, (int, float)):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            if not isinstance(div, (int, float)):
                raise TypeError("div must be a number")
            elif div == 0:
                raise ZeroDivisionError("division by zero")

            else:
                element = round(element / div, 2)
                new_list.append(element)
        my_matrix.append(new_list)

    return my_matrix
