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


if __name__ == '__main__':
    unittest.main()
