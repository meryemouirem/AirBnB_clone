#!/usr/bin/python3
""" unit test for Review """
import unittest
from models.review import Review
from datetime import datetime


class TestReview(unittest.TestCase):
    """ Test case for the Review class """

    attributes = ["id", "created_at", "updated_at", "place_id", "user_id", "text"]
    attribute_types = {"id": str, "created_at": datetime, "updated_at": datetime, "place_id": str, "user_id": str,
                       "text": str}

    def test_review(self):
        """ Test existence of required attributes """
        new = Review()
        for attr in self.attributes:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(new, attr))

        """ Test types of attributes """
        self.assertIsInstance(new.id, str)
        self.assertIsInstance(new.created_at, datetime)
        self.assertIsInstance(new.updated_at, datetime)
        self.assertIsInstance(new.place_id, str)
        self.assertIsInstance(new.user_id, str)
        self.assertIsInstance(new.text, str)


if __name__ == '__main__':
    unittest.main()
