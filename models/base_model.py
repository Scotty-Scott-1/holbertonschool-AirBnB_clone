#!/usr/bin/python3
"""Base console AirBnB"""


import uuid
from datetime import datetime
from models.engine.file_storage import FileStorage


class BaseModel:
    """class BaseModel that defines all common attributes/methods
    for other classes"""

    def __init__(self, *args, **kwargs):
        """initializes an instance of BaseModel"""
        if len(kwargs) < 1:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            self.id = kwargs.get("id", uuid.uuid4())
            self.created_at = kwargs.get("created_at")
            self.updated_at = kwargs.get("updated_at")


    def __str__(self):
        """prints a representation od the instance"""
        class_name = self.__class__.__name__
        return ("[{}] ({}) {}".format(class_name, self.id, self.__dict__))

    def save(self):
        """updates the public instance attribute updated_at with the
        current datetime"""

        self.updated_at = datetime.now()


    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of
        the instance"""

        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
