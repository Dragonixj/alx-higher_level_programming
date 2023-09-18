#!/usr/bin/python3
"""test cases for the base.py file
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
import os


class Test_Base(unittest.TestCase):
    """Class to evaluate different test cases for the base.py file"""

    def test_instance_type_id_class(self):
        """checks for the instance of the class"""
        b1 = Base()
        self.assertIsInstance(b1, Base)
        self.assertFalse(type(b1) == type(Base))
        self.assertFalse(id(b1) == id(Base))
        b2 = Base()
        self.assertTrue(type(b1) == type(b2))
        self.assertFalse(id(b1) == id(b2))
