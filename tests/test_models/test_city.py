#!/usr/bin/python3
""" unit test for City """
import unittest
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """ class for city test"""

     attributes = ["id", "created_at", "updated_at", "state_id", "name"]
    attribute_types = {"id": str, "created_at": datetime, "updated_at": datetime, "state_id": str, "name": str}

    def test_attributes_existence(self):
        """existence """
        new = City()
        for attr in self.attributes:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(new, attr))

    def test_attributes_types(self):

        """type test"""
        new = City()
        for attr, attr_type in self.attribute_types.items():
            with self.subTest(attr=attr):
                self.assertIsInstance(getattr(new, attr), attr_type)


if __name__ == '__main__':
    unittest.main()
