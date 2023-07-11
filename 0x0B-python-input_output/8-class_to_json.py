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
    if obj is not None:
        return
    keys = []
    for attr in obj.__dict__:
        if attr is not None:
            keys.append((attr, obj.__getattribute__(attr)))

    return dict(keys)
