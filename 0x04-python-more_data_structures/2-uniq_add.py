#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    new_list = set()
    for num in my_list:
        new_list.add(num)
    for num in new_list:
        sum += num
    return sum
