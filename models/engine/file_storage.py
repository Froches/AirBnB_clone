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
        return FileStorage.__objects

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        obj_dict = {key: obj.to_dict() for key,
                    obj in FileStorage.__objects.items()}
        with open(self.__file_path, 'w') as json_file:
            json.dump(obj_dict, json_file)

    def reload(self):
        try:
            with open(FileStorage.__file_path, 'r') as json_file:
                data = json.load(json_file)
                for key, obj_data in data.items():
                    cls_name, obj_id = key.split(".")
                    cls = FileStorage.__classes.get(cls_name)
                    if cls:
                        obj_inst = cls(**obj_data)
                        FileStorage.__objects[key] = obj_inst
        except (FileNotFoundError, json.JSONDecodeError):
            pass
