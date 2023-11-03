#!/usr/bin/python3
"""Test for class Place"""


import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage


class TestPlace(unittest.TestCase):
    def test_place_attributes(self):
        place = Place()
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_place_in_storage(self):
        place = Place()
        storage.save()
        key = "Place.{}".format(place.id)
        self.assertEqual(key in storage.all(), True)

    def test_place_set_and_get_name(self):
        place = Place()
        place.name = "laval"
        self.assertEqual(place.name, "laval")
        place.name = "paris"
        self.assertEqual(place.name, "paris")

    def test_city_inherits_from(self):
        self.assertTrue(issubclass(Place, BaseModel))


if __name__ == "__main__":
    unittest.main()
