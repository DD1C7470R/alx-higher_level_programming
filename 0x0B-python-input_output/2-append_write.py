#!/usr/bin/python3
""" Defines a function hat appends a string at the end of a
text file (UTF8) and returns the number of characters added
"""


def append_write(filename="", text=""):
    """ Defines a function hat appends a string at the end of a
    text file (UTF8) and returns the number of characters added
    """
    if not isinstance(filename, str):
        return

    if not isinstance(text, str):
        return

    if filename is None or len(filename) == 0:
        return ""

    with open(filename, mode='a', encoding='UTF8') as my_file:
        data = my_file.write(text)
        return data
