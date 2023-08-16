#!/usr/bin/python3
def search_replace(my_list, search, replace):

    if len(my_list) == 0:
        return None

    if search is None:
        return None

    if replace is None:
        return None
    
    final_list = my_list[:]
    for i in range(len(final_list)):
        if final_list[i] == search:
            final_list.remove(final_list[i])


            final_list.insert(i, replace)

    return final_list
