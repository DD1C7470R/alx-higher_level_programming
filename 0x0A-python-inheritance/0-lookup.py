#!usr/bin/python3
"""Defines a function that 
    returns the list of available attributes 
    and methods of an object
"""


def lookup(obj):
    """Defines a function that 
    returns the list of available attributes 
    and methods of an object
    """
    return [dir(obj)]



class MyClass1(object):
    pass

class MyClass2(object):
    my_attr1 = 3
    def my_meth(self):
        pass
