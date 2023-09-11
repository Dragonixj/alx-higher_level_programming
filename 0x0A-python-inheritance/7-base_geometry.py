#!/usr/bin/python3
"""
module that contains the BaseGeometry class
"""


class BaseGeometry:
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates tat the value is an integer and greater than 0"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
