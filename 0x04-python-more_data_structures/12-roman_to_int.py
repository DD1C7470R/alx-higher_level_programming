#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) != str:
        return 0
    sum = 0
    roman_numerals_table = {"I": 1, "V": 5, "X": 10, "L": 50,
                            "C": 100, "D": 500, "CM": 900, "M": 1000}
    for k in roman_string:
        if k in roman_numerals_table:
            sum += roman_numerals_table[k]
    return sum
