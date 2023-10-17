#!/usr/bin/python3
"""
Class thet serializes instances to a JSON file and deserializes JSON
files to instances
"""


import json
import os
import sys
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage():
    """
    The file storage class that serializes instances to a JSON file
    and deserializes JSON files to instances
    """

    __file_path = "file.json"
    __objects = {}
    __classes = {
            "BaseModel": BaseModel,
            "User": User,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Place": Place,
            "Review": Review
            }

    def __init__(self):
        """To initialize the class"""
        pass

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
            json.dump({key: obj.to_dict() for key,
                      obj in self.__objects.items()}, f)

    def reload(self):
        """Reloads saved instances"""
        if os.path.exists(self.__file_path):
            try:
                with open(self.__file_path, 'r') as f:
                    objs = json.load(f)
                    for key, obj in objs.items():
                        cls = key.split(".")[0]
                        obj_instance = self.__classes.get(cls)(**obj)
                        self.__objects[key] = obj_instance
            except FileNotFoundError:
                pass
