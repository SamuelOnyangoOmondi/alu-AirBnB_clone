#!/usr/bin/python3

"""Unittest for Amenity Class."""
import unittest
from models.amenity import Amenity
from models import BaseModel


class TestAmenity(unittest.TestCase):
    """Test cases for Amenity class."""

    def setUp(self):
        self.testAmenity = Amenity()

    def test_amenity(self):
        self.assertTrue(issubclass(self.testAmenity.__class__, BaseModel))

    def test_name(self):
        self.assertIsInstance(self.testAmenity.name, str)


if __name__ == "__main__":
    unittest.main()
