#!/usr/bin/python3
"""Define a function that
    reads a text file (UTF8) and prints it to stdout.
"""


def read_file(filename=""):
    """Define a function that
    reads a text file (UTF8) and prints it to stdout.
    """
    if filename is None or len(filename) == 0:
        return ""
    with open(filename, mode='r',  encoding="UTF8") as my_file:
        print(my_file.read())
