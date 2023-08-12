#!/usr/bin/python3
from sys import argv
from calculator_1 import add
if __name__ == "__main__":
    result = 0
    i = 1
    if len(argv) == 1:
        print(result)
    else:
        if len(argv) > 2:
            a = result
            while i < len(argv):
                result += int(argv[i])
                i += 1
            print(add(0, result))
