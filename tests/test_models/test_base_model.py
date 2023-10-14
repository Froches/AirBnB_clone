#!/usr/bin/python3
"""Testing the Base Model class"""
from models.base_model import BaseModel
import unittest
import os
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Class to test the edge cases of BaseModel"""

    def test_instantiation(self):
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

    def test_kwargs(self):
        model = BaseModel(arg1="value1", arg2="value2")
        self.assertEqual(model.arg1, "value1")
        self.assertEqual(model.arg2, "value2")

    def test_create_inst_with_default_values(self):
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertTrue(hasattr(model, 'id'))
        self.assertTrue(hasattr(model, 'created_at'))
        self.assertTrue(hasattr(model, 'updated_at'))
        self.assertEqual(type(model.created_at), datetime)
        self.assertEqual(type(model.updated_at), datetime)

    def test_create_inst_with_custom_values(self):
        custom_id = "custom_id"
        custom_created_at = "2023-10-10T12:00:00"
        custom_updated_at = "2023-10-10T13:00:00"

        model = BaseModel(id=custom_id, created_at=custom_created_at, updated_at=custom_updated_at)
        self.assertEqual(model.id, custom_id)
        self.assertEqual(model.created_at.isoformat(), custom_created_at)
        self.assertEqual(model.updated_at.isoformat(), custom_updated_at)

    def test_from_dict_method(self):
        custom_id = "custom_id"
        custom_created_at = "2023-10-10T12:00:00"
        custom_updated_at = "2023-10-10T13:00:00"

        model_dict = {
            '__class__': 'BaseModel',
            'id': custom_id,
            'created_at': custom_created_at,
            'updated_at': custom_updated_at
        }

        model = BaseModel(**model_dict)
        self.assertEqual(model.id, custom_id)
        self.assertEqual(model.created_at.isoformat(), custom_created_at)
        self.assertEqual(model.updated_at.isoformat(), custom_updated_at)

    def test_from_dict_with_invalid_class(self):
        custom_id = "custom_id"
        custom_created_at = "2023-10-10T12:00:00.00"
        custom_updated_at = "2023-10-10T13:00:00.00"

        model_dict = {
            '__class__': 'InvalidClass',
            'id': custom_id,
            'created_at': custom_created_at,
            'updated_at': custom_updated_at
        }

        with self.assertRaises(AttributeError):
            model = BaseModel(**model_dict)


if __name__ == '__main__':
    unittest.main()
