#!/usr/bin/python3
"""Defines a Rectangle class"""

from .base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""
    def __init__(self, width, height, x=0, y=0, id=None):
        if not type(width) == int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

        if not type(height) == int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

        if not type(x) == int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

        if not type(y) == int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    @property
    def width(self):
        """Get/setter for width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Get/setter for width"""
        if not type(value) == int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Get/setter for height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Get/setter for height"""
        if not type(value) == int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Get/setter for height"""
        return self.__x

    @x.setter
    def x(self, value):
        """Get/setter for height"""
        if not type(value) == int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Get/setter for height"""
        return self.__y

    @y.setter
    def y(self, value):
        """Get/setter for height"""
        if not type(value) == int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Defines the area of a rectangle"""
        return self.width * self.__height

    def display(self):
        """displays the area using space and #"""
        rows = 0
        for i in range(self.__y):
            print()
        while rows < self.__height:
            for i in range(self.__x):
                print(" ", end="")
            print("#" * self.width)

            rows += 1

    def __str__(self):
        return ("{} ({:d}) {}/{} - {}/{}"
                .format(
                    type(self).__name__, self.id,
                    self.__x, self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """Defines the update of a rectangle"""

        attr = ['id', 'width', 'height', 'x', 'y']
        if args:
            for idx, value in enumerate(args):
                setattr(self, attr[idx], value)
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Coverts a json string to a dictionary"""
        return (
            {
                'id': self.id, 'width': self.__width,
                'height': self.__height, 'x': self.__x,
                'y': self.__y
            })
