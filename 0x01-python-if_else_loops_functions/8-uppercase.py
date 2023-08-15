#!/usr/bin/python3
def uppercase(str):
    upper = ""
    for letter in str:
        if ord(letter) != 32:
            if ord(letter) >= 65 and ord(letter) <= 90:
                upper += letter
            elif ord(letter) <= 122 and ord(letter) >= 97:
                upper += chr(ord(letter) - 32)
            else:
                upper += letter
        else:
            upper += letter
    print("{}".format(upper))
