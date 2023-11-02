#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
import os
from models.base_model import BaseModel


classes = {'BaseModel': BaseModel}

class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls is None:
            return FileStorage.__objects
        else:
            new_dict = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    new_dict[key] = obj
            return new_dict

    def new(self, obj):
        """Adds a new object to storage dictionary"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to a file"""
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        """Loads storage dictionary from a file"""
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    self.all()[key] = classes[value['__class__']](**value)
