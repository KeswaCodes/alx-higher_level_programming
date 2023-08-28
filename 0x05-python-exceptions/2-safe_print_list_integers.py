#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num_printed = 0
        num_string = ""
        new_list = []
        for i in range(x):
            if isinstance(my_list[i], int):
                new_list.append(my_list[i])
                num_printed += 1

        for element in new_list:
            print("{:d}".format(element), end='')
        print("{}".format('\n'), end='')
    except IndexError:
        for element in new_list:
            print("{:d}".format(element), end='') 
        raise


    return num_printed
