#!/usr/bin/python3
"""
Consists of the TestReviewDocs instructions
"""

From datetime import datetime
Import investigate
From fashions import overview
From fashions.Base_model import BaseModel
Import pep8
Import unittest
Evaluation = review.Evaluation


Class TestReviewDocs(unittest.TestCase):
    """tests to test the documentation and style of review elegance"""
    @classmethod
    def setUpClass(cls):
        """installation for the document exams"""
        cls.Review_f = look into.Getmembers(review, check out.Isfunction)

    def test_pep8_conformance_review(self):
        """check that models/overview.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=genuine)
        end result = pep8s.Check_files(['models/review.Py'])
        self.AssertEqual(end result.Total_errors, 0,
                         "discovered code fashion mistakes (and warnings).")

    def test_pep8_conformance_test_review(self):
        """take a look at that assessments/test_models/test_review.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=true)
        end result = pep8s.Check_files(['tests/test_models/test_review.Py'])
        self.AssertEqual(end result.Total_errors, 0,
                         "found code fashion errors (and warnings).")

    def test_review_module_docstring(self):
        """take a look at for the evaluation.Py module docstring"""
        self.AssertIsNot(evaluation.__doc__, None,
                         "evaluate.Py wishes a docstring")
        self.AssertTrue(len(overview.__doc__) >= 1,
                        "evaluate.Py needs a docstring")

    def test_review_class_docstring(self):
        """test for the evaluation elegance docstring"""
        self.AssertIsNot(evaluate.__doc__, None,
                         "review magnificence desires a docstring")
        self.AssertTrue(len(assessment.__doc__) >= 1,
                        "evaluate elegance wishes a docstring")

    def test_review_func_docstrings(self):
        """take a look at for the presence of docstrings in evaluate methods"""
        for func in self.Review_f:
            self.AssertIsNot(func[1].__doc__, None,
                             ":s approach needs a docstring".Layout(func[0]))
            self.AssertTrue(len(func[1].__doc__) >= 1,
                            ":s technique desires a docstring".Format(func[0]))


Elegance TestReview(unittest.TestCase):
    """take a look at the assessment elegance"""
    def test_is_subclass(self):
        """test if evaluation is a subclass of BaseModel"""
        assessment = review()
        self.AssertIsInstance(overview, BaseModel)
        self.AssertTrue(hasattr(assessment, "id"))
        self.AssertTrue(hasattr(review, "created_at"))
        self.AssertTrue(hasattr(overview, "updated_at"))

    def test_place_id_attr(self):
        """test overview has attr place_id, and it is an empty string"""
        review = assessment()
        self.AssertTrue(hasattr(overview, "place_id"))
        self.AssertEqual(review.Place_id, "")

    def test_user_id_attr(self):
        """check evaluate has attr user_id, and it's an empty string"""
        evaluate = evaluate()
        self.AssertTrue(hasattr(overview, "user_id"))
        self.AssertEqual(assessment.User_id, "")

    def test_text_attr(self):
        """test review has attr textual content, and it is an empty string"""
        overview = overview()
        self.AssertTrue(hasattr(overview, "textual content"))
        self.AssertEqual(evaluate.Text, "")

    def test_to_dict_creates_dict(self):
        """take a look at to_dict technique creates a dictionary with right attrs"""
        r = overview()
        new_d = r.To_dict()
        self.AssertEqual(kind(new_d), dict)
        for attr in r.__dict__:
            self.AssertTrue(attr in new_d)
            self.AssertTrue("__class__" in new_d)

    def test_to_dict_values(self):
        """check that values in dict back from to_dict are accurate"""
        t_format = "%Y-%m-%dTpercentH:%M:%S.%f"
        r = assessment()
        new_d = r.To_dict()
        self.AssertEqual(new_d["__class__"], "assessment")
        self.AssertEqual(type(new_d["created_at"]), str)
        self.AssertEqual(type(new_d["updated_at"]), str)
        self.AssertEqual(new_d["created_at"], r.Created_at.Strftime(t_format))
        self.AssertEqual(new_d["updated_at"], r.Updated_at.Strftime(t_format))

    def test_str(self):
        """test that the str approach has the proper output"""
        assessment = overview()
        string = "[Review] () ".Layout(review.Identity, evaluation.__dict__)
        self.AssertEqual(string, str(review))
