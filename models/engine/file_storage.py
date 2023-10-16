#!/usr/bin/python3
"""
Class thet serializes instances to a JSON file and deserializes JSON
files to instances
"""
import json
import sys
from models.base_model import BaseModel


class FileStorage():
    """The file storage class"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns all instances"""
        return self.__objects

    def new(self, obj):
        """Creates new instance"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Saves created instances"""
        with open(self.__file_path, 'w') as f:
            json.dump({key: obj.to_dict() for key, obj in self.__objects.items()}, f)

    def reload(self):
        """Reloads saved instances"""
        if os.path.exists(self.__file_path):
            with open(self.__file_path, 'r') as f:
                objs = json.load(f)
            for key, obj in objs.items():
                if obj['__class__'] == 'User':
                    self.__objects[key] = User(**obj)
                else:
                    self.__objects[key] = BaseModel(**obj)
