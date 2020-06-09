#!/usr/bin/python3
""" test for the square """

import unittest
import json
import pep8
from models import square
from models.base import Base

class TestBase(unittest.TestCase):
    """ class for unit test """

    def test_id(self):
        """ test for the id """
        self.assertEqual(self.s1.id, 1)
        self.assertEqual(self.s2.id, 2)
        self.assertEqual(self.s3.id, 3)
        self.assertEqual(self.s4.id, 4)
        self.assertEqual(self.s5.id, 15)

    def test_size(self):
        """ test for size """
        self.assertEqual(self.s1.size, 1)
        self.assertEqual(self.s2.size, 4)
        self.assertEqual(self.s3.size, 7)
        self.assertEqual(self.s4.size, 9)

    def test_height(self):
        """ test for height """
        self.assertEqual(self.s1.height, 1)
        self.assertEqual(self.s2.height, 2)
        self.assertEqual(self.s3.height, 6)
        self.assertEqual(self.s4.height, 8)

    def test_width(self):
        """ test for width """
        self.assertEqual(self.s1.width, 1)
        self.assertEqual(self.s2.width, 5)
        self.assertEqual(self.s3.width, 7)
        self.assertEqual(self.s4.width, 9)

    def test_area(self):
        """ test for area """
        self.assertEqual(self.s1.area(), 1)
        self.assertEqual(self.s2.area(), 3)
        self.assertEqual(self.s3.area(), 5)
        self.assertEqual(self.s4.area(), 9)

    def test_x(self):
        """ test if x exists """
        self.assertEqual(self.s1.x, 0)
        self.assertEqual(self.s2.x, 5)
        self.assertEqual(self.s3.x, 7)
        self.assertEqual(self.s4.x, 10)

    def test_y(self):
        """ test for y """
        self.assertEqual(self.s1.y, 0)
        self.assertEqual(self.s2.y, 4)
        self.assertEqual(self.s3.y, 8)
        self.assertEqual(self.s1.x, 12)

