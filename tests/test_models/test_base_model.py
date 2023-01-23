"""
Checks the base model attributes
"""


From models.Base_model import BaseModel
Import unittest


Elegance TestBaseModel(unittest.TestCase):
    """
    assessments each aspect of advent of a base version
    """

    def setUp(self) -> None:
        self.B1 = BaseModel()
        self.B3 = BaseModel()
        self.B1_to_dict  = self.B1.To_dict()
        self.B2 = BaseModel(**self.B1_to_dict)

    def test_to_dict_method(self):
        """
        checks if the to_dict technique converts the basemodel to dictionary
        """
        self.AssertEqual(kind(self.B1_to_dict), dict)
    
    def test_to_dict(self):
        """testing to dict approach"""
        self.AssertIsInstance(self.B1_to_dict['updated_at'], str)

    def test_id_when_obj_created(self):
        """
        tests if an id is created when basemodel item is instantiated
        """

        self.AssertIsNotNone(self.B1.Identification)

    def test_obj_is_instance(self):
        """
        checks if the example b1 and b2 are times of BaseModel class
        """

        self.AssertIsInstance(self.B1, BaseModel);
        self.AssertIsInstance(self.B2, BaseModel)

    def test_str_(self):
        """ exams id __str__ prints a readable representation"""
        self.AssertEqual(str(self.B1), f"[self.B1.__class__.__name__] (self.B1.Identity) self.B1.__dict__") 

    def test_created_at_obj_created(self):
        self.AssertIsNotNone(self.B1.Created_at)

    def test_save(self):
        self.B1.Store()
        self.B3.Store()
        self.AssertNotEqual(self.B1.Updated_at, self.B3.Updated_at)


If __name__ == '__main__':
    unittest.Predominant()
