#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    if len(set_1) == 0 or len(set_2) == 0:
        return None

    set_3 = set_1.symmetric_difference(set_2)
    return set_3