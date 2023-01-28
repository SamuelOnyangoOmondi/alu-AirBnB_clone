#!/usr/bin/python3

"""Unittest for Review Class."""

import unittest

from models.review import Review

from models.base_model import BaseModel

class TestReview(unittest.TestCase):
"""Test cases Review class."""

def setUp(self):
    self.review = Review()

def test_instance(self):
    """test instance."""
    self.assertIsInstance(self.review, Review)

def test_is_class(self):
    """test instance."""
    self.assertEqual(str(type(self.review)),
                     "<class 'models.review.Review'>")

def test_is_subclass(self):
    """test is_subclass."""
    self.assertTrue(issubclass(type(self.review), BaseModel))

def test_text(self):
    """test is_subclass."""
    self.assertIsNotNone(self.review.id)
    self.assertEqual(self.review.text, "")
    self.assertEqual(self.review.user_id, "")
    self.assertEqual(self.review.place_id, "")

    if name == "main":
unittest.main()
