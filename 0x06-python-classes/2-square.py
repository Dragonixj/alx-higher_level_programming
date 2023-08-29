#!/usr/bin/python3
"""Defines a square"""


class Square:
    """Square with a private object attribute size"""

    def __init__(self, size):
        """
        Args:
            size: size of square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
        else:
            raise TypeError("size must be an integer")