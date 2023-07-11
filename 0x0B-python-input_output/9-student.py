#!/usr/bin/python3
""" Defines a function that returns the dictionary
 description with simple data structure
 (list, dictionary, string, integer and boolean)
 for JSON serialization of an obje
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Defines a function that returns the dictionary
        description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an obje
        """
        keys = []
        for attr in self.__dict__:
            if attr is not None:
                keys.append((attr, self.__getattribute__(attr)))

        return dict(keys)
