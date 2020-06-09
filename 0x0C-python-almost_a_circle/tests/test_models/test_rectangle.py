#!/usr/bin/python3
""" test for rectangle """


import unittest
import sys
import io
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
from os import path, remove
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """ unittest for rectangle """
    
    def t_height(self):
        """ test fot height """
        self.assertEqual(self.r1.height, 10)
        self.assertEqual(self.r2.height, 4)
        self.assertEqual(self.r3.height, 2)
        self.assertEqual(self.r4.height, 9)

    def t_width(self):
        """ test for widht """
        self.assertEqual(self.r1.width, 8)
        self.assertEqual(self.r2.width, 10)
        self.assertEqual(self.r3.width, 3)
        self.assertEqual(self.r4.width, 15)

    def t_y(self):
        """ test for y """
        self.assertEqual(self.r1.y, 0)
        self.assertEqual(self.r2.y, 6)
        self.assertEqual(self.r3.y, 9)
        self.assertEqual(self.r1.y, 13)

