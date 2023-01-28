#!/usr/bin/python3

"""Unittest for FileStorage Class."""

import os
import json
import unittest
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
"""Test cases for FileStorage class."""

# setUp Method called to prepare the test fixture. 
# This is called immediately before calling the test method
file_path = 'file.json'

def setUp(self):
    self.storage = FileStorage()

# Method to clean up resources that were created during the setup
def tearDown(self):
    if os.path.exists(self.file_path):
        os.remove(self.file_path)
    del self.storage

def test_instance(self):
    """test instance."""
    self.assertIsInstance(self.storage, FileStorage)

def test_is_class(self):
    """test instance."""
    self.assertEqual(str(type(self.storage)),
                     "<class 'models.engine.file_storage.FileStorage'>")

def test_file_path(self):
    """test file.json exits"""
    self.assertFalse(os.path.exists(self.file_path))
    self.storage.save()
    self.assertTrue(os.path.exists(self.file_path))

def test_objects(self):
    self.assertEqual(self.storage.all(), {})
    base = BaseModel()
    self.storage.new(base)
    self.assertIn(base, self.storage.all().values())

def test_all(self):
    """ test all."""
    self.assertEqual(type(self.storage.all()), dict)
    self.assertEqual(self.storage.all(), {})

def test_reload(self):
    """test reload"""
    self.storage.reload()
    self.assertIsInstance(self.storage.all(), type({}))

def test_reload_more(self):
    """test reload"""
    storage = FileStorage()
    storage.all().clear()
    storage.reload()
    self.assertEqual({}, self.storage.all())
    del storage

    class TestFileStorageReload(unittest.TestCase):
"""test again reload"""
file_path = 'file.json'

def setUp(self):
    self.storage = FileStorage()

def tearDown(self):
    if os.path.exists(self.file_path):
        os.remove(self.file_path)
    del self.storage

def test_reload(self):
    """test again reload"""
    base = BaseModel()
    base.save()

    self.storage.reload()

    object_key = "{}.{}".format(base.__class__.__name__, base.id)
    self.assertIn(object_key, self.storage.all())

    self.assertEqual(self.storage.all()[object_key].id, base.id)

    if name == "main":
un
