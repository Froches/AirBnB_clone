#!/usr/bin/python3
"""Base model class"""
import uuid
from datetime import datetime
import models
import sys


class BaseModel:
    """Base model class. Parent of all other subclasses"""

    def __init__(self, *args, **kwargs):
        """Initializes the BaseModel class"""

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            self.created_at = datetime.fromisoformat(self.created_at)
            self.updated_at = datetime.fromisoformat(self.updated_at)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """String representation of BaseModel class"""
        st = (f"[{self.__class__.__name__}] [{self.id}] {self.__dict__}")
        return st

    def save(self):
        """Update public inst attr 'updated_at' with current datetime"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing all key/values of instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
