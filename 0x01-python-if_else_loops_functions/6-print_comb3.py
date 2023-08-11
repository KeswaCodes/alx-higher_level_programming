#!/usr/bin/python3
numbers = " "
ignore = " "
for i in range(1, 89):
    if i < 10:
        i = "0" + str(i)
    numbers = numbers + str(i) + ", "
    while ignore > str(0):
        ignore = ignore + str(i % 10) + ", "
print("{}{}".format(i % 10, 1 % 10).lstrip(), end='')

