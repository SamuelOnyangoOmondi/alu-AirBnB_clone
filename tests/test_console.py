#!/usr/bin/python3
"""
Carries the class TestConsoleDocs
"""

Import console
From contextlib import redirect_stdout
Import check out
Import io
Import pep8
Import unittest
HBNBCommand = console.HBNBCommand


Magnificence TestConsoleDocs(unittest.TestCase):
    """class for checking out documentation of the console"""
    def test_pep8_conformance_console(self):
        """test that console.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=real)
        end result = pep8s.Check_files(['console.Py'])
        self.AssertEqual(result.Total_errors, 0,
                         "found code style mistakes (and warnings).")

    def test_pep8_conformance_test_console(self):
        """take a look at that tests/test_console.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=true)
        end result = pep8s.Check_files(['tests/test_console.Py'])
        self.AssertEqual(end result.Total_errors, 0,
                         "determined code fashion mistakes (and warnings).")

    def test_console_module_docstring(self):
        """check for the console.Py module docstring"""
        self.AssertIsNot(console.__doc__, None,
                         "console.Py wishes a docstring")
        self.AssertTrue(len(console.__doc__) >= 1,
                        "console.Py wishes a docstring")

    def test_HBNBCommand_class_docstring(self):
        """take a look at for the HBNBCommand elegance docstring"""
        self.AssertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand elegance wishes a docstring")
        self.AssertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand class wishes a docstring")


Class TestConsoleCommands(unittest.TestCase):
    """elegance to test functionality of console instructions"""
    @classmethod
    def setUpClass(cls):
        """Create command console to check with"""
        cls.Cmdcon = HBNBCommand()

    def setUp(self):
        """Create in memory buffer to seize stdout"""
        self.Output = io.StringIO()

    def tearDown(self):
        """near in reminiscence buffer after test completes"""
        self.Output.Close()

    def test_do_create(self):
        """check do_create technique of console"""
        with redirect_stdout(self.Output):
            self.Cmdcon.Onecmd('create')
            self.AssertEqual(self.Output.Getvalue(),
                             "** class call lacking **n")
            self.Output.Are seeking for(0)
            self.Output.Truncate()
            self.Cmdcon.Onecmd('create blah')
            self.AssertEqual(self.Output.Getvalue(),
                             "** magnificence doesn't exist **n")
            self.Output.Are seeking for(zero)
            self.Output.Truncate()
            self.Cmdcon.Onecmd('create country')
            self.AssertRegex(self.Output.Getvalue(),
                             '[a-z0-9]8-'
                             '[a-z0-9]four-'
                             '[a-z0-9]four-'
                             '[a-z0-9]four-'
                             '[a-z0-9]12')
            self.Output.Are trying to find(0)
            self.Output.Truncate()
            self.Cmdcon.Onecmd('create state name="California"')
            self.AssertRegex(self.Output.Getvalue(),
                             '[a-z0-9]8-'
                             '[a-z0-9]4-'
                             '[a-z0-9]4-'
                             '[a-z0-9]four-'
                             '[a-z0-9]12')
