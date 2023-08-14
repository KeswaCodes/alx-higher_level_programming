#!/usr/bin/python3
def no_c(my_string):
    # variables for resultant string to 'join' elements from string split
    new_string, new_string_2 = "", ""

    # lists declarations for resulting string splits
    list_of_upper_c, list_of_lower_c = [], []

    # split strings using 'c' & 'C' as delimiters & 'join' list into string
    list_of_upper_c = my_string.split('c')
    new_string = "".join(list_of_upper_c)
    list_of_lower_c = new_string.split('C')
    new_string_2 = "".join(list_of_lower_c)

    return new_string_2
