#!/usr/bin/python3
"""module that contains the class Base"""


class Base:
    """class Base is the base for all other classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Method that assigns the public instance attribute
        Args:
            id : is an integer
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
