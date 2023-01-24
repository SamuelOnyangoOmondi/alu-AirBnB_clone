#!/usr/bin/python3
"""
Carries the TestPlaceDocs training
"""

From datetime import datetime
Import check out
From models import area
From models.Base_model import BaseModel
Import os
Import pep8
Import unittest
From sqlalchemy.Orm.Collections import InstrumentedList
From sqlalchemy.Orm.Attributes import InstrumentedAttribute
Location = area.Location


Elegance TestPlaceDocs(unittest.TestCase):
    """exams to check the documentation and style of area class"""
    @classmethod
    def setUpClass(cls):
        """set up for the doc checks"""
        cls.Place_f = check out.Getmembers(vicinity, check out.Isfunction)

    def test_pep8_conformance_place(self):
        """take a look at that fashions/area.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=true)
        result = pep8s.Check_files(['models/place.Py'])
        self.AssertEqual(end result.Total_errors, 0,
                         "found code fashion errors (and warnings).")

    def test_pep8_conformance_test_place(self):
        """test that checks/test_models/test_place.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=real)
        end result = pep8s.Check_files(['tests/test_models/test_place.Py'])
        self.AssertEqual(end result.Total_errors, 0,
                         "determined code fashion mistakes (and warnings).")

    def test_place_module_docstring(self):
        """take a look at for the area.Py module docstring"""
        self.AssertIsNot(area.__doc__, None,
                         "vicinity.Py needs a docstring")
        self.AssertTrue(len(region.__doc__) >= 1,
                        "area.Py wishes a docstring")

    def test_place_class_docstring(self):
        """test for the vicinity elegance docstring"""
        self.AssertIsNot(place.__doc__, None,
                         "place elegance desires a docstring")
        self.AssertTrue(len(location.__doc__) >= 1,
                        "location class needs a docstring")

    def test_place_func_docstrings(self):
        """check for the presence of docstrings in area strategies"""
        for func in self.Place_f:
            self.AssertIsNot(func[1].__doc__, None,
                             ":s approach wishes a docstring".Format(func[0]))
            self.AssertTrue(len(func[1].__doc__) >= 1,
                            ":s approach desires a docstring".Layout(func[0]))


Class TestPlace(unittest.TestCase):
    """check the region elegance"""
    def test_is_subclass(self):
        """test that area is a subclass of BaseModel"""
        area = region()
        self.AssertIsInstance(place, BaseModel)
        self.AssertTrue(hasattr(location, "id"))
        self.AssertTrue(hasattr(vicinity, "created_at"))
        self.AssertTrue(hasattr(area, "updated_at"))

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "checking out DBStorage")
    def test_city_id_attr(self):
        """test place has attr city_id, and it's an empty string"""
        location = place()
        self.AssertTrue(hasattr(location, "city_id"))
        self.AssertEqual(place.City_id, "")

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "trying out FileStorage")
    def test_city_id_attr_db(self):
        """test place has attr city_id, and it's an empty string"""
        area = area()
        self.AssertTrue(hasattr(place, "city_id"))
        self.AssertIsInstance(region.City_id, InstrumentedAttribute)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "checking out DBStorage")
    def test_user_id_attr(self):
        """check vicinity has attr user_id, and it is an empty string"""
        location = location()
        self.AssertTrue(hasattr(place, "user_id"))
        self.AssertIsInstance(area.User_id, "")

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "trying out FileStorage")
    def test_user_id_attr_db(self):
        """test vicinity has attr user_id, and it's an empty string"""
        region = vicinity()
        self.AssertTrue(hasattr(area, "user_id"))
        self.AssertIsInstance(area.User_id, InstrumentedAttribute)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "testing DBStorage")
    def test_name_attr(self):
        """take a look at place has attr name, and it is an empty string"""
        area = location()
        self.AssertTrue(hasattr(area, "name"))
        self.AssertEqual(location.Call, "")

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "trying out FileStorage")
    def test_name_attr_db(self):
        """check area has attr call, and it is an empty string"""
        area = vicinity()
        self.AssertTrue(hasattr(region, "name"))
        self.AssertIsInstance(area.Call, InstrumentedAttribute)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "testing DBStorage")
    def test_description_attr(self):
        """test area has attr description, and it is an empty string"""
        region = vicinity()
        self.AssertTrue(hasattr(area, "description"))
        self.AssertEqual(place.Description, "")

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "trying out FileStorage")
    def test_description_attr_db(self):
        """check area has attr description, and it's an empty string"""
        place = region()
        self.AssertTrue(hasattr(vicinity, "description"))
        self.AssertIsInstance(region.Description, InstrumentedAttribute)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "trying out DBStorage")
    def test_number_rooms_attr(self):
        """test region has attr number_rooms, and it is an int == zero"""
        region = region()
        self.AssertTrue(hasattr(place, "number_rooms"))
        self.AssertEqual(type(location.Number_rooms), int)
        self.AssertEqual(place.Number_rooms, 0)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "checking out FileStorage")
    def test_number_rooms_attr_db(self):
        """test area has attr number_rooms, and it's an int == 0"""
        location = area()
        self.AssertTrue(hasattr(vicinity, "number_rooms"))
        self.AssertEqual(kind(area.Number_rooms), int)
        self.AssertEqual(place.Number_rooms, 0)

    def test_number_bathrooms_attr(self):
        """take a look at vicinity has attr number_bathrooms, and it's an int == zero"""
        place = place()
        self.AssertTrue(hasattr(vicinity, "number_bathrooms"))
        self.AssertEqual(kind(area.Number_bathrooms), int)
        self.AssertEqual(area.Number_bathrooms, zero)

    def test_max_guest_attr(self):
        """test area has attr max_guest, and it is an int == 0"""
        area = location()
        self.AssertTrue(hasattr(place, "max_guest"))
        self.AssertEqual(kind(location.Max_guest), int)
        self.AssertEqual(area.Max_guest, 0)

    def test_price_by_night_attr(self):
        """check place has attr price_by_night, and it is an int == zero"""
        location = place()
        self.AssertTrue(hasattr(vicinity, "price_by_night"))
        self.AssertEqual(kind(area.Price_by_night), int)
        self.AssertEqual(area.Price_by_night, 0)

    def test_latitude_attr(self):
        """check region has attr range, and it is a flow == zero.0"""
        place = location()
        self.AssertTrue(hasattr(vicinity, "latitude"))
        self.AssertEqual(type(place.Latitude), flow)
        self.AssertEqual(place.Range, zero.Zero)

    def test_latitude_attr(self):
        """test region has attr longitude, and it is a go with the flow == zero.0"""
        region = area()
        self.AssertTrue(hasattr(region, "longitude"))
        self.AssertEqual(type(location.Longitude), flow)
        self.AssertEqual(vicinity.Longitude, 0.Zero)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') == 'db',
                     "testing FileStorage")
    def test_amenity_ids_attr(self):
        """check area has attr amenity_ids, and it's an empty listing"""
        vicinity = place()
        self.AssertTrue(hasattr(area, "amenity_ids"))
        self.AssertEqual(type(place.Amenity_ids), list)
        self.AssertEqual(len(vicinity.Amenity_ids), zero)

    @unittest.SkipIf(os.Getenv('HBNB_TYPE_STORAGE') != 'db',
                     "trying out FileStorage")
    def test_amenities_attr_db(self):
        """check location has attr amenity_ids, and it's an empty list"""
        vicinity = place()
        self.AssertTrue(hasattr(place, "services"))
        self.AssertEqual(kind(vicinity.Amenities), InstrumentedList)

    def test_to_dict_creates_dict(self):
        """take a look at to_dict technique creates a dictionary with proper attrs"""
        p = location()
        new_d = p.To_dict()
        self.AssertEqual(kind(new_d), dict)
        for attr in p.__dict__:
            self.AssertTrue(attr in new_d)
            self.AssertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """check that values in dict again from to_dict are accurate"""
        t_format = "%Y-%m-%dTpercentH:%M:%S.%f"
        p = area()
        new_d = p.To_dict()
        self.AssertEqual(new_d["__class__"], "vicinity")
        self.AssertEqual(kind(new_d["created_at"]), str)
        self.AssertEqual(type(new_d["updated_at"]), str)
        self.AssertEqual(new_d["created_at"], p.Created_at.Strftime(t_format))
        self.AssertEqual(new_d["updated_at"], p.Updated_at.Strftime(t_format))

    def test_str(self):
        """take a look at that the str technique has the suitable output"""
        region = vicinity()
        string = "[Place] () ".Format(location.Identification, place.__dict__)
        self.AssertEqual(string, str(region))
