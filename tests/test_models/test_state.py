#!/usr/bin/python3
""" unit test for State class """

import unittest
from models.state import State
from datetime import datetime


class TestState(unittest.TestCase):
    """ Test cases for the State class """

    def setUp(self):
        """ Set up a State object for testing """
        self.new_state = State()
    def test_attributes_existence(self):
        """Test existence of required attributes"""
        attributes = ["id", "created_at", "updated_at", "name"]
        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.new_state, attr))
    def test_attributes_types(self):
        """Test types of attributes"""
        attribute_types = {"id": str, "created_at": datetime, "updated_at": datetime, "name": str}
        for attr, attr_type in attribute_types.items():
            with self.subTest(attr=attr):
                self.assertIsInstance(getattr(self.new_state, attr), attr_type)
    if __name__ == '__main__':
    unittest.main()
