#!/usr/bin/python3
"""Test for class City"""


import unittest
from models.city import City
from models.base_model import BaseModel
from models import storage


class TestCity(unittest.TestCase):
    def test_city_attributes(self):
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_city_in_storage(self):
        city = City()
        storage.save()
        key = "City.{}".format(city.id)
        self.assertEqual(key in storage.all(), True)

    def test_city_set_and_get_name(self):
        city = City()
        city.name = "laval"
        self.assertEqual(city.name, "laval")
        city.name = "paris"
        self.assertEqual(city.name, "paris")

    def test_city_inherits_from(self):
        self.assertTrue(issubclass(City, BaseModel))

if __name__ == "__main__":
    unittest.main()
