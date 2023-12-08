#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    A function that replaces all occurrences
    of an element by another in a new list
    """
    nw_list = []
    for element in my_list:
        if element == search:
            nw_list.append(replace)
        else:
            nw_list.append(element)
    return nw_list
