#!/usr/bin/python3
"""
Incorporates the TestUserDocs lessons
"""

From datetime import datetime
Import inspect
From models import user
From models.Base_model import BaseModel
Import pep8
Import unittest
User = consumer.Consumer


Elegance TestUserDocs(unittest.TestCase):
    """checks to check the documentation and style of consumer class"""
    @classmethod
    def setUpClass(cls):
        """installation for the doc tests"""
        cls.User_f = check out.Getmembers(consumer, look at.Isfunction)

    def test_pep8_conformance_user(self):
        """check that fashions/user.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=authentic)
        result = pep8s.Check_files(['models/user.Py'])
        self.AssertEqual(end result.Total_errors, 0,
                         "determined code fashion errors (and warnings).")

    def test_pep8_conformance_test_user(self):
        """check that checks/test_models/test_user.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=authentic)
        end result = pep8s.Check_files(['tests/test_models/test_user.Py'])
        self.AssertEqual(result.Total_errors, zero,
                         "found code fashion errors (and warnings).")

    def test_user_module_docstring(self):
        """take a look at for the user.Py module docstring"""
        self.AssertIsNot(person.__doc__, None,
                         "person.Py desires a docstring")
        self.AssertTrue(len(user.__doc__) >= 1,
                        "user.Py desires a docstring")

    def test_user_class_docstring(self):
        """take a look at for the city class docstring"""
        self.AssertIsNot(consumer.__doc__, None,
                         "user elegance needs a docstring")
        self.AssertTrue(len(consumer.__doc__) >= 1,
                        "user magnificence desires a docstring")

    def test_user_func_docstrings(self):
        """take a look at for the presence of docstrings in user methods"""
        for func in self.User_f:
            self.AssertIsNot(func[1].__doc__, None,
                             ":s technique wishes a docstring".Layout(func[0]))
            self.AssertTrue(len(func[1].__doc__) >= 1,
                            ":s technique desires a docstring".Format(func[0]))


Elegance TestUser(unittest.TestCase):
    """test the person magnificence"""
    def test_is_subclass(self):
        """take a look at that user is a subclass of BaseModel"""
        consumer = consumer()
        self.AssertIsInstance(user, BaseModel)
        self.AssertTrue(hasattr(person, "identity"))
        self.AssertTrue(hasattr(person, "created_at"))
        self.AssertTrue(hasattr(person, "updated_at"))

    def test_email_attr(self):
        """test that user has attr e-mail, and it's an empty string"""
        person = consumer()
        self.AssertTrue(hasattr(person, "e mail"))
        self.AssertEqual(person.E mail, "")

    def test_password_attr(self):
        """check that person has attr password, and it is an empty string"""
        person = user()
        self.AssertTrue(hasattr(person, "password"))
        self.AssertEqual(consumer.Password, "")

    def test_first_name_attr(self):
        """check that person has attr first_name, and it's an empty string"""
        user = person()
        self.AssertTrue(hasattr(person, "first_name"))
        self.AssertEqual(consumer.First_name, "")

    def test_last_name_attr(self):
        """check that person has attr last_name, and it's an empty string"""
        user = user()
        self.AssertTrue(hasattr(user, "last_name"))
        self.AssertEqual(user.Last_name, "")

    def test_to_dict_creates_dict(self):
        """test to_dict technique creates a dictionary with proper attrs"""
        u = person()
        new_d = u.To_dict()
        self.AssertEqual(kind(new_d), dict)
        for attr in u.__dict__:
            self.AssertTrue(attr in new_d)
            self.AssertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """take a look at that values in dict again from to_dict are accurate"""
        t_format = "%Y-%m-%dTp.CH:%M:%S.%f"
        u = person()
        new_d = u.To_dict()
        self.AssertEqual(new_d["__class__"], "consumer")
        self.AssertEqual(kind(new_d["created_at"]), str)
        self.AssertEqual(type(new_d["updated_at"]), str)
        self.AssertEqual(new_d["created_at"], u.Created_at.Strftime(t_format))
        self.AssertEqual(new_d["updated_at"], u.Updated_at.Strftime(t_format))

    def test_str(self):
        """take a look at that the str technique has an appropriate output"""
        consumer = person()
        string = "[User] () ".Layout(user.Identity, consumer.__dict__)
        self.AssertEqual(string, str(user))
