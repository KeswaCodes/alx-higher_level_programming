#!/usr/bin/python3
import sys
if __name__ == "__main__":
    i = 1
    args = len(sys.argv)
    args -= 1
    if (len(sys.argv) == 1):
        print("{} arguments".format(args))

    else:
        print("{} arguments:".format(args))
        while i <= args:
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
