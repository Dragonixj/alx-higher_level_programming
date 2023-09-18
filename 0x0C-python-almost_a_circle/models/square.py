#!/usr/bin/python3
"""Module that defines a square object"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Method that initialises the square
        Args:
            size: size of the sides of a square
            x: position on the x axis
            y: position on the y axis
        Return:
            Always nothing"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Method that returns a string"""
        return "[Square] ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """Getter of the size"""
        return self.width

    @size.setter
    def size(self, value):
        """Setter of the size
        Args:
           value: Size to assign
        Return:
           always Nothing
        """
        self.width = value
        self.heigth = value
