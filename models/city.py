#!/usr/bin/python3
from model.base_model import BaseModel


class City(BaseModel):
    """City class that inherits from BaseModel"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.State.id = ""
        self.name = ""
