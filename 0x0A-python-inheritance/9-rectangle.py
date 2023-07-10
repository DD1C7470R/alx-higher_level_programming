#!/usr/bin/python3
"""Defines a class Rectangle that inherits from BaseGeometry
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """a class Rectangle that inherits from BaseGeometry
    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Get/set width values
        """
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = width

    @property
    def height(self):
        """Get/set height values
        """
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = height

    def area(self):
        """Calculates the area of the rectangle
        """
        return self.width * self.height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.width, self.height)
