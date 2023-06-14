#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) != str:
        return 0
    sum_val = 0
    prev = 0
    roman_table = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000
    }
    for k in reversed(roman_string):
        if k in roman_table:
            val = roman_table.get(k, 0)
            if val >= prev:
                sum_val += val
            else:
                sum_val -= val
        prev = val
    return sum_val
