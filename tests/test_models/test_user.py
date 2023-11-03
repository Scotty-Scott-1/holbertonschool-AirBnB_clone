#!/usr/bin/python3
"""Test for class User"""


import unittest
from models.user import User
from models.base_model import BaseModel
from models import storage


class TestUser(unittest.TestCase):
    def test_user_attributes(self):
        user = User()
        self.assertEqual(user.email, "")
        self.assertEqual(user.password, "")
        self.assertEqual(user.first_name, "")
        self.assertEqual(user.last_name, "")

    def test_user_in_storage(self):
        user = User()
        storage.save()
        key = "User.{}".format(user.id)
        self.assertEqual(key in storage.all(), True)

    def test_review_set_and_get_name(self):
        user = User()
        user.email = "1"
        user.password = "2"
        user.first_name = "3"
        user.last_name = "4"
        self.assertEqual(user.email, "1")
        self.assertEqual(user.password, "2")
        self.assertEqual(user.first_name, "3")
        self.assertEqual(user.last_name, "4")
        user.email = "5"
        user.password = "6"
        user.first_name = "7"
        user.last_name = "8"
        self.assertEqual(user.email, "5")
        self.assertEqual(user.password, "6")
        self.assertEqual(user.first_name, "7")
        self.assertEqual(user.last_name, "8")

    def test_user_inherits_from(self):
        self.assertTrue(issubclass(User, BaseModel))


if __name__ == "__main__":
    unittest.main()
