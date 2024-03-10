#!/usr/bin/python3
""" unit test for Amenity """

import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ class for amenity test """


    def setUp(self):

        self.new_amenity = Amenity()

    def test_attributes_existence(self):
        """existince"""
        attributes = ["id", "created_at", "updated_at", "name"]
        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.new_amenity, attr))
    def test_attributes_types(self):
        """type test"""
        attribute_types = {"id": str, "created_at": datetime, "updated_at": datetime, "name": str}
        for attr, attr_type in attribute_types.items():
            with self.subTest(attr=attr):
                self.assertIsInstance(getattr(self.new_amenity, attr), attr_type)


if __name__ == '__main__':
    unittest.main()
