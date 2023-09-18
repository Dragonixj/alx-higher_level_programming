#!/usr/bin/python3
"""module that contains class Rectanglele inheriting from Base(models.base)"""
from models.base import Base


class Rectangle(Base):
    """Defines a Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Method that initiates the values for the rectangle object
        Args:
            width: the widht size
            height: the height size
            x: variable x
            y: variable y
        Return:
            returns nothing"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    # The getter and setter for the width
    @property
    def width(self):
        """The getter size of the width."""
        return self._width

    @width.setter
    def width(self, value):
        """setter size of the width
        Args:
            value: size to assign to the width
        Return:
            returns nothing
        """
        self.__width = value

    # The getter and setter for the height
    @property
    def height(self):
        """The height."""
        return self._height

    @height.setter
    def height(self, value):
        """setter size of the height
        Args:
            value: size to assign to the height
        Return:
            returns nothing"""
        self.__height = value
