#!/usr/bin/python3
""" unittests for models/user.py """
import unittest
from models.user import User
from datetime import datetime


class TestUser(unittest.TestCase):
    """ Test cases for the User clas """

    def setUp(self):
        """ Set up a User object for testing """
        self.new_user = User()

    def test_attributes_existence(self):
        """ Test existence of required attributes """

        self.assertTrue(hasattr(self.new_user, "id"))
        self.assertTrue(hasattr(self.new_user, "created_at"))
        self.assertTrue(hasattr(self.new_user, "updated_at"))
        self.assertTrue(hasattr(self.new_user, "email"))
        self.assertTrue(hasattr(self.new_user, "password"))
        self.assertTrue(hasattr(self.new_user, "first_name"))
        self.assertTrue(hasattr(self.new_user, "last_name"))

        """ Test types of attributes """
        self.assertIsInstance(self.new_user.id, str)
        self.assertIsInstance(self.new_user.created_at, datetime)
        self.assertIsInstance(self.new_user.updated_at, datetime)
        self.assertIsInstance(self.new_user.email, str)
        self.assertIsInstance(self.new_user.password, str)
        self.assertIsInstance(self.new_user.first_name, str)
        self.assertIsInstance(self.new_user.last_name, str)


if __name__ == '__main__':
    unittest.main()
