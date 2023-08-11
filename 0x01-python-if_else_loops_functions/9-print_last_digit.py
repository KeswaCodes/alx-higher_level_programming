#!/usr/bin/python3
def print_last_digit(number):

    last_digit = ""

    if number < 0:
        number = number * -1
        last_digit += str(number % 10)
    else:
        last_digit += str(number % 10)
    print("{}".format(last_digit), end='')
