#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    printed_numbers = 0
    for i in range(list_length):
        try:
            division = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            division = 0

        except IndexError:
            print("out of range")
            division = 0
        except TypeError:
            print("wrong type")
            division = 0

        finally:
            new_list.append(division)
            pass
    return new_list
