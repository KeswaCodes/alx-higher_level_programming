#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    if len(a_dictionary) == 0:
        return None

    keys = list(a_dictionary.keys())
    highest = a_dictionary.get(keys[0])
    
    for key in keys:
       check = a_dictionary.get(key, None)
       if check is None:
           return None

       if check > highest:
           highest = check
           key_highest = key


    return key_highest
