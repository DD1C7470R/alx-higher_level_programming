#!/usr/bin/python3
""" Test function find_peak """


def find_peak(my_list):
    """ Defines the function find peak"""
    if len(my_list) == 0:
        return None

    left, right = 0, len(my_list) - 1

    while left < right:
        mid = left + (right - left) // 2
        if my_list[mid] > my_list[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return my_list[left]

