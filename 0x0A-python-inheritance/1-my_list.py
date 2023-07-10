#!/usr/bin/python3
"""Defines a class MyList that inherits from list
"""


class MyList(list):
    """Defines a class MyList that inherits from list
    """
    def __init__(self, A):
        super().__init__()
        self.A = A

    def print_sorted(self):
        return sorted(self.A)
