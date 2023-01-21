#!/usr/bin/python3
"""test BaseModel for expected behavior and documentation"""
From datetime import datetime
Import check out
Import models
Import os
Import pep8 as pycodestyle
Import time
Import unittest
From unittest import mock
BaseModel = models.Base_model.BaseModel
Module_doc = fashions.Base_model.__doc__


Magnificence TestBaseModelDocs(unittest.TestCase):
    """assessments to test the documentation and fashion of BaseModel elegance"""

    @classmethod
    def setUpClass(self):
        """installation for docstring tests"""
        self.Base_funcs = check out.Getmembers(BaseModel, look at.Isfunction)

    def test_pep8_conformance(self):
        """take a look at that models/base_model.Py conforms to PEP8."""
        for route in ['models/base_model.Py',
                     'tests/test_models/test_base_model.Py']:
            with self.SubTest(course=course):
                errors = pycodestyle.Checker(course).Check_all()
                self.AssertEqual(errors, zero)

    def test_module_docstring(self):
        """take a look at for the life of module docstring"""
        self.AssertIsNot(module_doc, None,
                         "base_model.Py wishes a docstring")
        self.AssertTrue(len(module_doc) > 1,
                        "base_model.Py desires a docstring")

    def test_class_docstring(self):
        """test for the BaseModel elegance docstring"""
        self.AssertIsNot(BaseModel.__doc__, None,
                         "BaseModel class needs a docstring")
        self.AssertTrue(len(BaseModel.__doc__) >= 1,
                        "BaseModel magnificence needs a docstring")

    def test_func_docstrings(self):
        """test for the presence of docstrings in BaseModel methods"""
        for func in self.Base_funcs:
            with self.SubTest(feature=func):
                self.AssertIsNot(
                    func[1].__doc__,
                    None,
                    ":s method wishes a docstring".Format(func[0])
                )
                self.AssertTrue(
                    len(func[1].__doc__) > 1,
                    ":s technique needs a docstring".Format(func[0])
                )


Class TestBaseModel(unittest.TestCase):
    """check the BaseModel class"""
    def test_instantiation(self):
        """take a look at that item is effectively created"""
        inst = BaseModel()
        self.AssertIs(type(inst), BaseModel)
        inst.Name = "Holberton"
        inst.Wide variety = 89
        attrs_types = 
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
            "call": str,
            "quantity": int
        
        for attr, typ in attrs_types.Items():
            with self.SubTest(attr=attr, typ=typ):
                self.AssertIn(attr, inst.__dict__)
                self.AssertIs(type(inst.__dict__[attr]), typ)
        self.AssertEqual(inst.Name, "Holberton")
        self.AssertEqual(inst.Wide variety, 89)

    def test_datetime_attributes(self):
        """take a look at that two BaseModel times have unique datetime objects
        and that upon advent have equal updated_at and created_at
        price."""
        tic = datetime.Now()
        inst1 = BaseModel()
        toc = datetime.Now()
        self.AssertTrue(tic <= inst1.Created_at <= toc)
        time.Sleep(1e-four)
        tic = datetime.Now()
        inst2 = BaseModel()
        toc = datetime.Now()
        self.AssertTrue(tic <= inst2.Created_at <= toc)
        self.AssertEqual(inst1.Created_at, inst1.Updated_at)
        self.AssertEqual(inst2.Created_at, inst2.Updated_at)
        self.AssertNotEqual(inst1.Created_at, inst2.Created_at)
        self.AssertNotEqual(inst1.Updated_at, inst2.Updated_at)

    def test_uuid(self):
        """take a look at that identification is a valid uuid"""
        inst1 = BaseModel()
        inst2 = BaseModel()
        for inst in [inst1, inst2]:
            uuid = inst.Identification
            with self.SubTest(uuid=uuid):
                self.AssertIs(type(uuid), str)
                self.AssertRegex(uuid,
                                 '^[0-9a-f]eight-[0-9a-f]four'
                                 '-[0-9a-f]four-[0-9a-f]four'
                                 '-[0-9a-f]12$')
        self.AssertNotEqual(inst1.Identification, inst2.Id)

    def test_to_dict(self):
        """check conversion of item attributes to dictionary for json"""
        my_model = BaseModel()
        my_model.Call = "Holberton"
        my_model.My_number = 89
        d = my_model.To_dict()
        expected_attrs = ["id",
                          "created_at",
                          "updated_at",
                          "name",
                          "my_number",
                          "__class__"]
        self.AssertCountEqual(d.Keys(), expected_attrs)
        self.AssertEqual(d['__class__'], 'BaseModel')
        self.AssertEqual(d['name'], "Holberton")
        self.AssertEqual(d['my_number'], 89)
        self.AssertNotIn('_sa_instance_state', d)

    def test_to_dict_values(self):
        """check that values in dict back from to_dict are accurate"""
        t_format = "%Y-%m-%dTpercentH:%M:%S.%f"
        bm = BaseModel()
        new_d = bm.To_dict()
        self.AssertEqual(new_d["__class__"], "BaseModel")
        self.AssertEqual(kind(new_d["created_at"]), str)
        self.AssertEqual(kind(new_d["updated_at"]), str)
        self.AssertEqual(new_d["created_at"], bm.Created_at.Strftime(t_format))
        self.AssertEqual(new_d["updated_at"], bm.Updated_at.Strftime(t_format))

    def test_str(self):
        """test that the str technique has the appropriate output"""
        inst = BaseModel()
        string = "[BaseModel] () ".Format(inst.Identity, inst.__dict__)
        self.AssertEqual(string, str(inst))

    @mock.Patch('fashions.Storage')
    def test_save(self, mock_storage):
        """check that store method updates `updated_at` and calls
        `garage.Keep`"""
        inst = BaseModel()
        old_created_at = inst.Created_at
        old_updated_at = inst.Updated_at
        inst.Shop()
        new_created_at = inst.Created_at
        new_updated_at = inst.Updated_at
        self.AssertNotEqual(old_updated_at, new_updated_at)
        self.AssertEqual(old_created_at, new_created_at)
        self.AssertTrue(mock_storage.New.Referred to as)
        self.AssertTrue(mock_storage.Shop.Called)
