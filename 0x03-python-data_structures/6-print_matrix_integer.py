#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix is None:
        return

# loop through each row in the matrix
    for row in matrix:
        new_string = ""
        my_list = []
# add each element in the row to a string
        for element in row:
            new_string += str(element)
# append each element of the string to list
        for i in new_string:
            my_list.append(i)
# use 'join' to add space at the end of each digit
        new_string = " ".join(my_list)
        print("{}".format(new_string))
