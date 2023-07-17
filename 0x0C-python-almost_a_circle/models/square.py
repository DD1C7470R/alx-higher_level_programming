#!/usr/bin/python3
"""Defines a Square class"""

from .rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("{} ({:d}) {}/{} - {:d}"
                .format(
                    type(self).__name__, self.id,
                    self.x, self.y, self.width
                    )
                )

    @property
    def size(self):
        """Get/set for size"""
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates the instance attributess of a square class"""
        attr = ['id', 'size', 'x', 'y']
        if args:
            for idx, value in enumerate(args):
                setattr(self, attr[idx], value)
        else:
            if kwargs:
                for key, value in kwargs.items():
                    setattr(self, key, value)

    def to_dictionary(self):
        """Converts class attributes to dictionary form"""
        return (
            {
                'id': self.id, 'size': self.size,
                'x': self.x, 'y': self.y
            })
