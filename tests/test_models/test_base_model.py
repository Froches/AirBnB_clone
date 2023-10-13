#!/usr/bin/python3
"""Testing the Base Model class"""
from models.base_model import BaseModel
import unittest
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test the edge cases of BaseModel"""

    def test_instantiation(self):
        """Test if an instance of BaseModel is created successfully"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)

    def test_uuid(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_unique_id(self):
        """Testif he UUIDs generated for different instances of BaseModel are unique"""
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_created_at(self):
        model = BaseModel()
        self.assertIsInstance(model.created_at, datetime)

    def test_updated_at(self):
        model = BaseModel()
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        model = BaseModel()
        expected_str = f"[BaseModel] [{model.id}] {model.__dict__}"
        self.assertEqual(str(model), expected_str)

    def test_save(self):
        """Test if 'updated_at' is updated after calling save"""
        model = BaseModel()
        old_updated_at = model.updated_at
        model.save()
        self.assertNotEqual(old_updated_at, model.updated_at)

    def test_to_dict(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertTrue(isinstance(model_dict, dict))
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        self.assertEqual(model_dict['__class__'], "BaseModel")

    def test_iso_format(self):
        model = BaseModel()
        iso_format = model.created_at.isoformat()
        self.assertEqual(iso_format, model.created_at.isoformat())

    def test_id_string(self):
        model = BaseModel()
        self.assertIsInstance(model.id, str)

    def test_args(self):
        model = BaseModel("argument1", "argument2")
        self.assertEqual(model.argument1, "argument1")
        self.assertEqual(model.argument2, "argument2")

    def test_instantiation_with_args(self):
        model = BaseModel(1, 2, 3)
        self.assertEqual(model.args, (1, 2, 3))

    def test_kwargs(self):
        model = BaseModel(arg1="value1", arg2="value2")
        self.assertEqual(model.arg1, "value1")
        self.assertEqual(model.arg2, "value2")

    def test_instantiation_with_kwargs(self):
        model = BaseModel(arg1 = "value1", arg2 = "value2")
        self.assertEqual(model.kwargs, {"arg1": "value1", "arg2": "value2"})

    def test_save_update_files(self):
        model = BaseModel()
        model.save()
        filename = "file.json"
        with open(filename, 'r') as file:
            data = file.read()
            self.assertIn(model.id, data)
            self.assertIn(model.created_at.isoformat(), data)
            self.assertIn(model.__class__.__name__, data)


if __name__ == '__main__':
    unittest.main()
