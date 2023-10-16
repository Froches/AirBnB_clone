#!/usr/bin/python3
"""
Class thet serializes instances to a JSON file and deserializes JSON
files to instances
"""
import json
import sys
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


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
            try:
                with open(self.__file_path, 'r') as f:
                    objs = json.load(f)
                for key, obj in objs.items():
                    if obj['__class__'] == 'BaseModel':
                        self.__objects[key] = BaseModel(**obj)
                    elif obj['__class__'] == 'User':
                        self.__objects[key] = User(**obj)
                    elif obj['__class__'] == 'State':
                        self.__objects[key] = State(**obj)
                    elif obj['__class__'] == 'City':
                        self.__objects[key] = City(**obj)
                    elif obj['__class__'] == 'Amenity':
                        self.__objects[key] = Amenity(**obj)
                    elif obj['__class__'] == 'Place':
                        self.__objects[key] = Place(**obj)
                    elif obj['__class__'] == 'Review':
                        self.__objects[key] = Review(**obj)
            except FileNotFoundError:
            pass
