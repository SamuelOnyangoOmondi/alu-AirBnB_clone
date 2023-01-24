#!/usr/bin/python3
"""
Consists of the TestStateDocs lessons
"""

From datetime import datetime
Import look at
From models import nation
From models.Base_model import BaseModel
Import pep8
Import unittest
Kingdom = nation.Country


Class TestStateDocs(unittest.TestCase):
    """tests to check the documentation and fashion of state elegance"""
    @classmethod
    def setUpClass(cls):
        """installation for the document tests"""
        cls.State_f = look into.Getmembers(state, look into.Isfunction)

    def test_pep8_conformance_state(self):
        """check that models/country.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=actual)
        end result = pep8s.Check_files(['models/state.Py'])
        self.AssertEqual(result.Total_errors, zero,
                         "found code style mistakes (and warnings).")

    def test_pep8_conformance_test_state(self):
        """check that exams/test_models/test_state.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=real)
        end result = pep8s.Check_files(['tests/test_models/test_state.Py'])
        self.AssertEqual(result.Total_errors, 0,
                         "discovered code style errors (and warnings).")

    def test_state_module_docstring(self):
        """take a look at for the kingdom.Py module docstring"""
        self.AssertIsNot(country.__doc__, None,
                         "nation.Py desires a docstring")
        self.AssertTrue(len(state.__doc__) >= 1,
                        "country.Py wishes a docstring")

    def test_state_class_docstring(self):
        """check for the nation elegance docstring"""
        self.AssertIsNot(state.__doc__, None,
                         "kingdom class desires a docstring")
        self.AssertTrue(len(state.__doc__) >= 1,
                        "kingdom magnificence desires a docstring")

    def test_state_func_docstrings(self):
        """take a look at for the presence of docstrings in state methods"""
        for func in self.State_f:
            self.AssertIsNot(func[1].__doc__, None,
                             ":s method needs a docstring".Layout(func[0]))
            self.AssertTrue(len(func[1].__doc__) >= 1,
                            ":s method desires a docstring".Layout(func[0]))


Elegance TestState(unittest.TestCase):
    """check the nation magnificence"""
    def test_is_subclass(self):
        """check that country is a subclass of BaseModel"""
        state = country()
        self.AssertIsInstance(nation, BaseModel)
        self.AssertTrue(hasattr(country, "identity"))
        self.AssertTrue(hasattr(country, "created_at"))
        self.AssertTrue(hasattr(country, "updated_at"))

    def test_name_attr(self):
        """take a look at that state has characteristic call, and it is as an empty string"""
        nation = state()
        self.AssertTrue(hasattr(state, "call"))
        self.AssertEqual(nation.Call, "")

    def test_to_dict_creates_dict(self):
        """take a look at to_dict method creates a dictionary with right attrs"""
        s = state()
        new_d = s.To_dict()
        self.AssertEqual(kind(new_d), dict)
        for attr in s.__dict__:
            self.AssertTrue(attr in new_d)
            self.AssertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """check that values in dict returned from to_dict are accurate"""
        t_format = "%Y-%m-%dTpercentH:%M:%S.%f"
        s = country()
        new_d = s.To_dict()
        self.AssertEqual(new_d["__class__"], "nation")
        self.AssertEqual(type(new_d["created_at"]), str)
        self.AssertEqual(type(new_d["updated_at"]), str)
        self.AssertEqual(new_d["created_at"], s.Created_at.Strftime(t_format))
        self.AssertEqual(new_d["updated_at"], s.Updated_at.Strftime(t_format))

    def test_str(self):
        """check that the str method has an appropriate output"""
        kingdom = nation()
        string = "[State] () ".Format(nation.Identification, state.__dict__)
        self.AssertEqual(string, str(country))
