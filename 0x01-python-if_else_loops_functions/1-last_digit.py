#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
greater_than_5 = "and is greater than 5"
less_than_6_not_0 = "and is less than 6 and not 0"
equal_to_0 = "and is 0"


if (number < 0):
    number = number * -1
    last_digit = number % 10
    negative_number = "-" + str(last_digit)
    if int(negative_number) < 6 and int(negative_number) != 0:
        print(f"Last digit of -{number} is -{last_digit} {less_than_6_not_0}")
    elif negative_number > 5:
        print(f"Last digit of -{number} is -{last_digit} {greater_than_5}")

    else:
        print(f"Last digit of -{number} is -{last_digit} {equal_to_0}")

else:
    last_digit = number % 10
    if last_digit < 6 and last_digit != 0:
        print(f"Last digit of {number} is {last_digit} {less_than_6_not_0}")
    elif last_digit > 5:
        print(f"Last digit of {number} is {last_digit} {greater_than_5}")

    else:
        print(f"Last digit of {number} is {last_digit} {equal_to_0}")
