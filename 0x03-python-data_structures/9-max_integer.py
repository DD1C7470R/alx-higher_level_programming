#!/usr/bin/python3

def max_integer(my_list=[]):
    list_size = len(my_list)
    if (list_size == 0):
        return (None)

    sortedList = sorted(my_list)
    max_num = sortedList[list_size - 1]
    return (max_num)
