#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    A function that adds all unique
    integers in a list (only once for each integer)
    """
    nw_list = []
    sum = 0
    for num in my_list:
        if num not in nw_list:
            sum += num
            nw_list.append(num)
    return sum
