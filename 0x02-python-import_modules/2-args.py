#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    i = 1
    args = len(argv)
    args -= 1
    if len(argv) == 1:
        print("{} arguments.".format(args))

    else:
        if args == 1:
            print("{} argument:".format(args))
            print("{}: {}".format(args, argv[args]))

        else:
            print("{} arguments:".format(args))
            while i <= args:
                print("{}: {}".format(i, argv[i]))
                i += 1
