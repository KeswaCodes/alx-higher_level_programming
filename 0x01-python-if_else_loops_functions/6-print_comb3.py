#!/usr/bin/python3
numbers, num_2 = " ", " "
for i in range(0, 99):
    if i < 10:
        i = "0" + str(i)
        
    numbers = numbers + str(i) + ", "
numbers_list = numbers.split(",")

for element in numbers_list:
    if element == element[0] * 2:
        continue
    num_2 = num_2 + element + ", "
print("{}".format(num_2.lstrip()), end='')
print("{}".format(99))
