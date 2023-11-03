#!/usr/bin/python3
"""Test for class Review"""


import unittest
from models.review import Review
from models.base_model import BaseModel
from models import storage


class TestReview(unittest.TestCase):
    def test_review_attributes(self):
        review = Review()
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_review_in_storage(self):
        review = Review()
        storage.save()
        key = "Review.{}".format(review.id)
        self.assertEqual(key in storage.all(), True)

    def test_review_set_and_get_name(self):
        review = Review()
        review.text = "laval"
        self.assertEqual(review.text, "laval")
        review.text = "paris"
        self.assertEqual(review.text, "paris")

    def test_review_inherits_from(self):
        self.assertTrue(issubclass(Review, BaseModel))


if __name__ == "__main__":
    unittest.main()
