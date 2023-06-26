#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        sum = 0
        sum = a / b
    except ZeroDivisionError:
        sum = None
    finally:
        print("Inside result: {}".format(sum))
    return sum
