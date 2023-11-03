#!/usr/bin/python3
"""Test for class Amenity"""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from models import storage


class TestAmenity(unittest.TestCase):
    def test_amenity_attributes(self):
        amenity = Amenity()
        self.assertEqual(amenity.name, "")

    def test_amenity_in_storage(self):
        amenity = Amenity()
        storage.save()
        key = "Amenity.{}".format(amenity.id)
        self.assertEqual(key in storage.all(), True)

    def test_amenity_set_and_get_name(self):
        amenity = Amenity()
        amenity.name = "shop"
        self.assertEqual(amenity.name, "shop")
        amenity.name = "park"
        self.assertEqual(amenity.name, "park")

    def test_amenity_inherits_from(self):
        self.assertTrue(issubclass(Amenity, BaseModel))


if __name__ == "__main__":
    unittest.main()
