#!/usr/bin/python3
"""User cclass that inherits from BaseModel"""
from models.base_model import BaseModel


class User(BaseModel):
    """User class is a child class from base class-BaseModel"""

def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.email = ""
    self.password = ""
    self.first_name = ""
    self.last_name = ""