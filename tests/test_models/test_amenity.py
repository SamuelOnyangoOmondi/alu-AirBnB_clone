#!/usr/bin/python3
"""
Contains the TestAmenityDocs classes
"""

from datetime import datetime
import inspect
from models import amenity
from models.base_model import BaseModel
import os
import pep8
import unittest
from sqlalchemy.orm.attributes import InstrumentedAttribute
Amenity = amenity.Amenity


class TestAmenityDocs(unittest.TestCase):
    """Tests to check the documentation and style of Amenity class"""
    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.amenity_f = inspect.getmembers(Amenity, inspect.isfunction)

    def test_pep8_conformance_amenity(self):
        """Test that models/amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['models/amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_pep8_conformance_test_amenity(self):
        """Test that tests/test_models/test_amenity.py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=True)
        result = pep8s.check_files(['tests/test_models/test_amenity.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_amenity_module_docstring(self):
        """Test for the amenity.py module docstring"""
        self.assertIsNot(amenity.__doc__, None,
                         "amenity.py needs a docstring")
        self.assertTrue(len(amenity.__doc__) >= 1,
                        "amenity.py needs a docstring")

    def test_amenity_class_docstring(self):
        """Test for the Amenity class docstring"""
        self.assertIsNot(Amenity.__doc__, None,
                         "Amenity class needs a docstring")
        self.assertTrue(len(Amenity.__doc__) >= 1,
                        "Amenity class needs a docstring")

    def test_amenity_func_docstrings(self):
        """Test for the presence of docstrings in Amenity methods"""
        for func in self.amenity_f:
            self.assertIsNot(func[1].__doc__, None,
                             "{:s} method needs a docstring".format(func[0]))
            self.assertTrue(len(func[1].__doc__) >= 1,
                            "{:s} method needs a docstring".format(func[0]))


class TestAmenity(unittest.TestCase):
    def test_is_subclass(self):
        """Test that Amenity is a subclass of BaseModel"""
        amenity_instance = Amenity()
        self.assertIsInstance(amenity_instance, BaseModel)
        self.assertTrue(hasattr(amenity_instance, "id"))
        self.assertTrue(hasattr(amenity_instance, "created_at"))
        self.assertTrue(hasattr(amenity_instance, "updated_at"))

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db',
                     "Testing DBStorage")
    def test_name_attr(self):
        """Test that Amenity has attribute name, and it's as an empty string"""
        amenity_instance = Amenity()
        self.assertTrue(hasattr(amenity_instance, "name"))
        self.assertEqual(amenity_instance.name, "")

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') != 'db',
                     "Testing FileStorage")
    def test_name_attr_db(self):
        """Test for DBStorage name attribute"""
        amenity_instance = Amenity()
        self.assertTrue(hasattr(Amenity, "name"))
        self.assertIsInstance(Amenity.name, InstrumentedAttribute)

    def test_to_dict_creates_dict(self):
        """test to_dict method creates a dictionary with proper attributes"""
        am = Amenity()
        new_dict = am.to_dict()
        self.assertEqual(type(new_dict), dict)
        for attr in am.__dict__:
            with self.subTest(attr=attr):
                if attr == '_sa_instance_state':
                    continue
                self.assertTrue(attr in new_dict)
        if os.getenv('HBNB_TYPE_STORAGE') != 'db':
            self.assertTrue("__class__" in new_dict)

    def test_to_dict_values(self):
        """test that values in dictionary returned from to_dict are correct"""
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        am = Amenity()
        new_dict = am.to_dict()
        self.assertEqual(new_dict["__class__"], "Amenity")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"], am.created_at.strftime(time_format))
        self.assertEqual(new_dict["updated_at"], am.updated_at.strftime(time_format))

    def test_str(self):
        """test that the str method has the correct output"""
        amenity_instance = Amenity()
        string = "[Amenity] ({}) {}".format(amenity_instance.id, amenity_instance.__dict__)
        self.assertEqual(string, str(amenity))

