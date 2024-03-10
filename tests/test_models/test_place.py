#!/usr/bin/python3
""" unit test for Review """
import unittest
from models.place import Place
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ class for place test """
    def test_place(self):
        """Test existence of required attributes """
        attributes = [
            "id", "created_at", "updated_at", "city_id", "user_id",
            "name", "description", "number_rooms", "number_bathrooms",
            "max_guest", "price_by_night", "latitude", "longitude",
            "amenity_ids"
        ]

        for attr in attributes:
            with self.subTest(attr=attr):
                self.assertTrue(hasattr(self.new_place, attr))
    def test_attributes_types(self):
        """type test """
        attribute_types = {
                "id": str, "created_at": datetime, "updated_at": datetime,
                "city_id": str, "user_id": str, "name": str,
                "description": str, "number_rooms": int,
                "number_bathrooms": int, "max_guest": int,
                "price_by_night": int, "latitude": float,
                "longitude": float, "amenity_ids": list
                }
        for attr, attr_type in attribute_types.items():
            with self.subTest(attr=attr):
                self.assertIsInstance(getattr(self.new_place, attr), attr_type)
if __name__ == '__main__':
    unittest.main()
