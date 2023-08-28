#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        list_len = 0
        i = 0
        string = ""
        while i < x:
            string += "".join(str(my_list[i]))
            i += 1
            list_len += 1
        print("{}".format(string))

    except IndexError:
        print("{}".format(string))

    finally:

        return list_len
