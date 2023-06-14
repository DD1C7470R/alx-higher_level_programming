#!/usr/bin/python3

def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) == 0:
        return None
    max_val = 0
    key = ''
    for k, v in a_dictionary.items():
        if v > max_val:
            max_val = v
            key = k
    return key
