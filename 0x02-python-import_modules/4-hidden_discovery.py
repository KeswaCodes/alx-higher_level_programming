#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    i = 0
    name = dir(hidden_4)
    name_len = len(name)
    while i < name_len:
        if name[i][0:2] == '__':
            i += 1
            continue
        else:
            print(name[i])
        i += 1
