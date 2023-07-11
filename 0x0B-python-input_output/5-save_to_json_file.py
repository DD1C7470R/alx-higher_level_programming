#!/usr/bin/python3
""" Defines a function  writes
an Object to a text file, using a JSON representation
"""


import json


def save_to_json_file(my_obj, filename):
    """ Defines a function  writes an Object
    to a text file, using a JSON representation
    """

    with open(filename, mode='w') as my_file:
        my_file.write(json.dumps(my_obj))
