#!/usr/bin/python3
""" Test function find_peak """


def find_peak(my_list):
    """ Defines the function find peak"""
    if len(my_list) == 0:
        return None

    peak_val = my_list[0]
    for val in my_list:
        if val > peak_val:
            peak_val = val
    return peak_val
