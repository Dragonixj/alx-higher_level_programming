#!/usr/bin/python3
"""The mylist class"""


class Mylist(list):
    """Inherits from list class"""

    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        print(sorted(self))
