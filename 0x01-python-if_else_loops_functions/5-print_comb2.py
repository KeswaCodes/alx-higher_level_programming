#!/usr/bin/python3
numbers = " "
for i in range(0, 99):
    if i < 10:
        i = "0" + str(i)
    numbers = numbers + str(i) + ", "
print("{}".format(numbers).lstrip(), end='')
print("{}".format(99))
