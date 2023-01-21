#!/usr/bin/python3
"""
Carries the TestCityDocs classes
"""

From datetime import datetime
Import inspect
From fashions import city
From fashions.Base_model import BaseModel
Import os
Import pep8
Import unittest
From sqlalchemy.Orm.Attributes import InstrumentedAttribute
City = metropolis.Town


Elegance TestCityDocs(unittest.TestCase):
    """tests to test the documentation and fashion of town elegance"""
    @classmethod
    def setUpClass(cls):
        """set up for the document checks"""
        cls.City_f = look into.Getmembers(city, look into.Isfunction)

    def test_pep8_conformance_city(self):
        """take a look at that models/metropolis.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=authentic)
        end result = pep8s.Check_files(['models/city.Py'])
        self.AssertEqual(result.Total_errors, zero,
                         "located code style errors (and warnings).")

    def test_pep8_conformance_test_city(self):
        """check that exams/test_models/test_city.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=actual)
        result = pep8s.Check_files(['tests/test_models/test_city.Py'])
        self.AssertEqual(result.Total_errors, zero,
                         "found code fashion errors (and warnings).")

    def test_city_module_docstring(self):
        """test for the city.Py module docstring"""
        self.AssertIsNot(city.__doc__, None,
                         "town.Py needs a docstring")
        self.AssertTrue(len(town.__doc__) >= 1,
                        "city.Py needs a docstring")

    def test_city_class_docstring(self):
        """test for the town class docstring"""
        self.AssertIsNot(city.__doc__, None,
                         "city elegance wishes a docstring")
        self.AssertTrue(len(town.__doc__) >= 1,
                        "metropolis class desires a docstring")

    def test_city_func_docstrings(self):
        """check for the presence of docstrings in metropolis strategies"""
        for func in self.City_f:
            self.AssertIsNot(func[1].__doc__, None,
                             ":s method wishes a docstring".Layout(func[0]))
            self.AssertTrue(len(func[1].__doc__) >= 1,
                            ":s method wishes a docstring".Layout(func[0]))


Class TestCity(unittest.TestCase):
    """take a look at the metropolis class"""
    def test_is_subclass(self):
        """check that town is a subclass of BaseModel"""
        metropolis = town()
        self.AssertIsInstance(city, BaseModel)
        self.AssertTrue(hasattr(town, "identity"))
        self.AssertTrue(hasattr(city, "created_at"))
        self.AssertTrue(hasattr(city, "updated_at"))

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "checking out DBStorage")
    def test_name_attr(self):
        """check that city has attribute name, and it is an empty string"""
        metropolis = city()
        self.AssertTrue(hasattr(city, "name"))
        self.AssertEqual(metropolis.Name, "")

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "trying out FileStorage")
    def test_name_attr_db(self):
        """take a look at for DBStorage call characteristic"""
        city = city()
        self.AssertTrue(hasattr(metropolis, "name"))
        self.AssertIsInstance(city.Call, InstrumentedAttribute)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "trying out DBStorage")
    def test_state_id_attr(self):
        """check that town has attribute state_id, and it's an empty string"""
        town = town()
        self.AssertTrue(hasattr(city, "state_id"))
        self.AssertEqual(city.State_id, "")

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "trying out FileStorage")
    def test_state_id_attr_db(self):
        """check for DBStorage state_id characteristic"""
        city = town()
        self.AssertTrue(hasattr(metropolis, "state_id"))
        self.AssertIsInstance(town.State_id, InstrumentedAttribute)

    def test_to_dict_creates_dict(self):
        """take a look at to_dict method creates a dictionary with right attrs"""
        c = metropolis()
        new_d = c.To_dict()
        self.AssertEqual(type(new_d), dict)
        for attr in c.__dict__:
            with self.SubTest(attr=attr):
                if attr == '_sa_instance_state':
                    preserve
                self.AssertTrue(attr in new_d)
        if os.Getenv('HBNB_TYPE_STORAGE') != 'db':
            self.AssertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """check that values in dict returned from to_dict are accurate"""
        t_format = "%Y-%m-%dTpercentH:%M:%S.%f"
        c = city()
        new_d = c.To_dict()
        self.AssertEqual(new_d["__class__"], "metropolis")
        self.AssertEqual(kind(new_d["created_at"]), str)
        self.AssertEqual(kind(new_d["updated_at"]), str)
        self.AssertEqual(new_d["created_at"], c.Created_at.Strftime(t_format))
        self.AssertEqual(new_d["updated_at"], c.Updated_at.Strftime(t_format))

    def test_str(self):
        """test that the str approach has an appropriate output"""
        city = metropolis()
        string = "[City] () ".Layout(metropolis.Identity, city.__dict__)
        self.AssertEqual(string, str(metropolis))
