#!/usr/bin/python3
""" Defines a function that returns the dictionary
 description with simple data structure
 (list, dictionary, string, integer and boolean)
 for JSON serialization of an object
"""


class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Defines a function that returns the dictionary
        description with simple data structure
        (list, dictionary, string, integer and boolean)
        for JSON serialization of an object
        """
        json = []
        if isinstance(attrs, list):
            for attr in attrs:
                if type(attr) == str:
                    if hasattr(self, attr):
                        json.append((attr, self.__getattribute__(attr)))
        else:
            for attr in self.__dict__:
                if attr is not None:
                    json.append((attr, self.__getattribute__(attr)))

        return dict(json)

    def reload_from_json(self, json):
        self.__dict__ = json
