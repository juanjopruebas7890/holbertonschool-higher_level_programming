#!/usr/bin/python3
""" Unittest
"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ unittest """
    def test_without_arg(self):
        """ in case no argument is passed """
        self.assertIsNone(max_integer())

    def test_negative_num(self):
        """ test negative number """
        ls = [-5, -13, -23, -45]
        self.assertEqual(max_integer(ls), -5)

    def test_alone_number(self):
        """ test alone num in list """
        ls = [9]
        self.assertEqual(max(ls), 9)

    def test_float_num(self):
        """ test float """
        ls = [2.0, 3.0, 5.0, 8.0]
        self.assertEqual(max_integer(ls), 8.0)

    def test_two_max_num(self):
        """ test two max #"""
        ls = [1, 2, 6, 6, 3]
        self.assertEqual(max_integer(ls), 6)

    def test_none(self):
        """ test if none is passed """
        ls = []
        self.assertEqual(max_integer(ls), None)

if __name__ == "__main__":
    unittest.main()
