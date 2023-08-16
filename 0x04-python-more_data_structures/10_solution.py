#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    if len(a_dictionary) == 0:
        return None
# get a list of tuples from dictionary
    list_of_tuples = list(a_dictionary.items())
    highest = list_of_tuples[0][1]

# loop through tuple list to find highest value
    for i in range(len(list_of_tuples)):
        if type(list_of_tuples[i][1]) is not int:
            return None
        if list_of_tuples[i][1] > highest:
            highest = list_of_tuples[i][1]

# index to the highest value
    key = list_of_tuples[i - 1][0]
    return key
