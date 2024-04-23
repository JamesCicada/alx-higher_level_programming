#!/usr/bin/python3
"""
Unit tests for Base class
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    Class for unit testing Base class
    """
    def test_id_generation(self):
        """
        Test Base ID generation
        """
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_id_generation_twice(self):
        """
        Test Base ID generation twice
        """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_generation_third(self):
        """
        Test Base ID generation third time
        """
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 2)

    def test_id_with_argument(self):
        """
        Test Base ID generation with argument
        """
        b = Base(12)
        self.assertEqual(b.id, 12)

    def test_id_with_none(self):
        """
        Test Base ID generation with None
        """
        b1 = Base(None)
        b2 = Base(None)
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_mix(self):
        """
        Test Base ID generation with mix of arguments
        """
        b1 = Base()
        b2 = Base(12)
        b3 = Base()
        self.assertEqual(b1.id, b3.id - 1)

    def test_change_id_value(self):
        """
        Test changing Base ID value
        """
        b = Base(12)
        b.id = 15
        self.assertEqual(15, b.id)

    def test_base_with_two_arguments(self):
        """
        Test Base with two arguments
        """
        with self.assertRaises(TypeError):
            Base(1, 1)

if __name__ == "__main__":
    unittest.main()
