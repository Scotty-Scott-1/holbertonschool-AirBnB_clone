#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""


import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity

classes = {
    'BaseModel': BaseModel,
    'User': User,
    'City': City,
    'State': State,
    'Review': Review,
    'Place': Place,
    'Amenity': Amenity
}


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        if cls is None:
            return FileStorage.__objects
        else:
            new_dict = {}
            for key, obj in FileStorage.__objects.items():
                if isinstance(obj, cls):
                    new_dict[key] = obj
            return new_dict

    def new(self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        serialized_objects = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objects, file)

    def reload(self):
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    if class_name in classes:
                        obj = classes[class_name](**value)
                        FileStorage.__objects[key] = obj
