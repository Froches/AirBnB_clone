#!/usr/bin/python3
"""Base model class"""
import uuid
from datetime import datetime


class BaseModel:
    """Base model class. Parent of all other subclasses"""

    def __init__(self, *args, **kwargs):
        """Initializes T=the BaseModel class"""
        if kwargs:
            if '__class__' in kwargs:
                kwargs.pop('__class__')
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """String representation of BaseModel class"""
        st=(f"[{self.__class__.__name__}] [{self.id}] {self.__dict__}")
        return st
    
    def save(self):
        """Update public inst attr 'updated_at' with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all key/values of instance"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
