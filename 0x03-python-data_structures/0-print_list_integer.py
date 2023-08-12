#!/usr/bin/python3

def print_list_integer(my_list=[]):
    for item in range(1, len(my_list) + 1):
        result = "{}".format(item)
        print(result)
if __name__ == "__main__":
    print_list_integer()
