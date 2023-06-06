#!/usr/bin/python3
def print_last_digit(number):
    if number is None:
        return
    else:
        last_digit = abs(number) % 10

    print("{}".format(last_digit), end="")
    return last_digit
