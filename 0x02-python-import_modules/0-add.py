#!/usr/bin/python3
from add_0 import add as module

if __name__ == "__main__":
    a = 1
    b = 2
    result = module.add(a, b)
    print("{} + {} = {}".format(a, b, result))
