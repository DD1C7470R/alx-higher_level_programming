#!/usr/bin/python3
""" Defines a function that returns the dictionary
 description with simple data structure
 (list, dictionary, string, integer and boolean)
 for JSON serialization of an obje
"""


def class_to_json(obj):
    """ Defines a function that returns the dictionary
    description with simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an obje
    """

    json = obj.__dict__
    return json
