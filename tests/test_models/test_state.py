#!/usr/bin/python3
"""Test for class State"""


import unittest
from models.state import State
from models.base_model import BaseModel
from models import storage


class TestState(unittest.TestCase):
    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_in_storage(self):
        state = State()
        storage.save()
        key = "State.{}".format(state.id)
        self.assertEqual(key in storage.all(), True)

    def test_state_set_and_get_name(self):
        state = State()
        state.name = "laval"
        self.assertEqual(state.name, "laval")
        state.name = "paris"
        self.assertEqual(state.name, "paris")

    def test_review_inherits_from(self):
        self.assertTrue(issubclass(State, BaseModel))


if __name__ == "__main__":
    unittest.main()
