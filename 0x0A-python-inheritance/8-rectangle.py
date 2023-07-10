#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry
"""


class BaseGeometry:
    """Defines an empty class BaseGeometry
    """
    def __init__(self):
        pass

    def area(self):
        """Defines an empty class BaseGeometry
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates class Rectangle parameter values
        """
        if not isinstance(value, int) or not type(value) == int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
        else:
            pass


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """A reprresentation of Rectangle."""
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
