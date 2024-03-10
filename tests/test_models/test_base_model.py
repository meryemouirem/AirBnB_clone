#!/usr/bin/python3
""" Test Suite for Base Model Functionality """
import json
import unittest
from models.base_model import BaseModel
from datetime import datetime
import models
from io import StringIO
import sys
from unittest.mock import patch

captured_output = StringIO()
sys.stdout = captured_output


class BaseModelTestCase(unittest.TestCase):
    """Test cases for BaseModel class functionality """

    def setUp(self):
        """ Set up test environment """
        self.filepath = models.storage._FileStorage__file_path
        with open(self.filepath, 'w') as file:
            file.truncate(0)
        models.storage.all().clear()

    def tearDown(self):
        """ Clean up after each test """
        printed_output = captured_output.getvalue()
        sys.stdout = sys.__stdout__

    def test_basemodel_init(self):
        """ Test BaseModel initialization and attribute existence """
        new_instance = BaseModel()
        """ check if it have methods """
        self.assertTrue(hasattr(new_instance, "__init__"))
        self.assertTrue(hasattr(new_instance, "__str__"))
        self.assertTrue(hasattr(new_instance, "save"))
        self.assertTrue(hasattr(new_instance, "to_dict"))

        """existence"""
        self.assertTrue(hasattr(new_instance, "id"))
        self.assertTrue(hasattr(new_instance, "created_at"))
        self.assertTrue(hasattr(new_instance, "updated_at"))

        """type test"""
        self.assertIsInstance(new_instance.id, str)
        self.assertIsInstance(new_instance.created_at, datetime)
        self.assertIsInstance(new_instance.updated_at, datetime)

        """ check if save in storage """
        keyname = "BaseModel." + new_instance.id
        self.assertIn(keyname, models.storage.all())
        self.assertTrue(models.storage.all()[keyname] is new_instance)

        """ Test update """
        new_instance.name = "My First Model"
        new_instance.my_number = 89
        self.assertTrue(hasattr(new_instance, "name"))
        self.assertTrue(hasattr(new_instance, "my_number"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "name"))
        self.assertTrue(hasattr(models.storage.all()[keyname], "my_number"))

        """check if save() update update_at """
        old_time = new_instance.updated_at
        new_instance.save()
        self.assertNotEqual(old_time, new_instance.updated_at)
        self.assertGreater(new_instance.updated_at, old_time)

        """ check if 'save' method calls: models.storage.save() """
        with patch('models.storage.save') as mock_function:
            obj = BaseModel()
            obj.save()
            mock_function.assert_called_once()

        """check if object is saved in json file"""
        keyname = "BaseModel." + new_instance.id
        with open(self.filepath, 'r') as file:
            saved_data = json.load(file)
        """ check if object exist by keyname """
        self.assertIn(keyname, saved_data)
        """ check if the value found in json is correct"""
        self.assertEqual(saved_data[keyname], new_instance.to_dict())

    def test_base_model_initialization_from_dict(self):
        """ Test BaseModel initialization from dictionary """

        new = BaseModel()
        new.name = "John"
        new.my_number = 89

        new2 = BaseModel(**new.to_dict())

        self.assertEqual(new.id, new2.id)
        self.assertEqual(new.name, "John")
        self.assertEqual(new.my_number, 89)
        self.assertEqual(new.to_dict(), new2.to_dict())

    def test_base_model_initialization_different_instances(self):
        """ Test initialization of different BaseModel instances """
        instance1 = BaseModel()
        instance2 = BaseModel(instance1.to_dict())
        self.assertNotEqual(instance1, instance2)
        self.assertNotEqual(instance1.id, instance2.id)
        self.assertTrue(isinstance(instance2.created_at, datetime))
        self.assertTrue(isinstance(instance2.updated_at, datetime))

        instance = BaseModel()

        self.assertEqual(
            str(instance1), "[BaseModel] ({}) {}".format(instance1.id, instance1.__dict__))

        old_time = instance1.updated_at
        instance1.save()
        self.assertGreater(instance1.updated_at, old_time)


if __name__ == '__main__':
    unittest.main()
