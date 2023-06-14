#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) != str:
        return 0
    sum_val = 0
    prev = ''
    roman_table = {
            "I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
            "D": 500, "M": 1000
    }
    for k in roman_string:
        if k in roman_table:
            if prev != '':
                if roman_table[k] > roman_table[prev]:
                    sum_val = roman_table[k] - roman_table[prev]
                    prev = k
                else:
                    sum_val += roman_table[k]
                    prev = k
            else:
                sum_val += roman_table[k]
                prev = k
    return sum_val
