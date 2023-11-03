#!/usr/bin/python3
"""Unittest for FileStorage"""


import unittest
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.review import Review
from models.place import Place
from models.amenity import Amenity
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    def setUp(self):
        self.storage = FileStorage()

    def test_all(self):
        self.assertIsInstance(self.storage.all(), dict)

    def test_new(self):
        new_user = User()
        self.storage.new(new_user)
        key = "User.{}".format(new_user.id)
        self.assertEqual(self.storage.all()[key], new_user)

    def test_save_reload(self):
        new_user = User()
        self.storage.new(new_user)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        key = "User.{}".format(new_user.id)
        self.assertEqual(loaded_storage.all()[key].to_dict(),
                         new_user.to_dict())

    def tearDown(self):
            try:
                os.remove(FileStorage._FileStorage__file_path)
            except:
                pass

    def delete(self, obj=None):
        """Deletes an object from storage if it exists"""
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]
                self.save()

    def test_load_multiple_classes(self):
        new_user = User()
        new_city = City()
        new_state = State()
        self.storage.new(new_user)
        self.storage.new(new_city)
        self.storage.new(new_state)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        key_user = "User.{}".format(new_user.id)
        key_city = "City.{}".format(new_city.id)
        key_state = "State.{}".format(new_state.id)
        self.assertEqual(loaded_storage.all()[key_user].to_dict(),
                         new_user.to_dict())
        self.assertEqual(loaded_storage.all()[key_city].to_dict(),
                         new_city.to_dict())
        self.assertEqual(loaded_storage.all()[key_state].to_dict(),
                         new_state.to_dict())

    def test_load_empty_file(self):
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertEqual(len(loaded_storage.all()), len(self.storage.all()))

    def test_load_non_existent_file(self):
        self.storage._FileStorage__file_path = "non_existent_file.json"
        loaded_storage = FileStorage()
        loaded_storage.reload()
        self.assertEqual(len(loaded_storage.all()), len(self.storage.all()))

    def test_save_custom_file_path(self):
        self.storage._FileStorage__file_path = "custom_file.json"
        new_user = User()
        self.storage.new(new_user)
        self.storage.save()
        loaded_storage = FileStorage()
        loaded_storage._FileStorage__file_path = "custom_file.json"
        loaded_storage.reload()
        key = "User.{}".format(new_user.id)
        self.assertEqual(loaded_storage.all()[key].to_dict(),
                         new_user.to_dict())


if __name__ == '__main__':
    unittest.main()
