#!/usr/bin/python3
def print_last_digit(number):
    if number is None:
        return
    else:
        last_digit = abs(number) % 10
        if number < 0:
            last_digit = -(last_digit)
    print("{}".format(last_digit), end="")
    return last_digit
