#!/usr/bin/python3
num_string = ""
# loop through all number combinatiosn to create a string of combinations
for first_digit in range(0, 9):
    for second_digit in range(1, 10):
        digit = str(first_digit) + str(second_digit) + " "
        num_string += digit
# a list to hold the string of all possible combinations
num_list = []
num_list = num_string.split()

# create a list to store all double digits & reverse combinations
double_digit_list, reverse_digit_list = [], []

final_string = ""
final_list = []

# loop through combination list to add non-double & on-reverse digits
for element in num_list:
    # create list of reverse digits
    reverse_digit = str(element[1]) + str(element[0])
    reverse_digit_list.append(reverse_digit)

# create list of double digits
    double_digit = element[0] * 2
    double_digit_list.append(double_digit)

    if element in double_digit_list or element in reverse_digit_list:
        continue
# append non-reverse/ non-double digit element to final list
    else:
        final_list.append(element)
# create final string for the final list of non-reverse & non-double digits
final_string = ", ".join(final_list)
print(final_string)
