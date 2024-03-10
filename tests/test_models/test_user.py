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

        self.assertTrue(hasattr(new, "id"))
        self.assertTrue(hasattr(new, "created_at"))
        self.assertTrue(hasattr(new, "updated_at"))
        self.assertTrue(hasattr(new, "email"))
        self.assertTrue(hasattr(new, "password"))
        self.assertTrue(hasattr(new, "first_name"))
        self.assertTrue(hasattr(new, "last_name"))

        """ Test types of attributes """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.email, str)
        self.assertIsInstance(new.password, str)
        self.assertIsInstance(new.first_name, str)
        self.assertIsInstance(new.last_name, str)


if __name__ == '__main__':
    unittest.main()
