#!/usr/bin/python3

"""Unittest for Amenity Class."""

import unittest

from models.city import City


class TestCity(unittest.TestCase):
    """Test cases City class."""

    def setUp(self):
        self.testCity = City()

    def test_is_class(self):
        """test instance."""
        self.assertIsInstance(self.testCity.state_id, str)

    def test_is_subclass(self):
        self.assertIsInstance(self.testCity.name, str)


if __name__ == "__main__":
    unittest.main()
