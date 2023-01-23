#!/usr/bin/python3
"""
Contains the magnificence TestConsoleDocs
"""

Import console
From contextlib import redirect_stdout
Import check out
Import io
Import pep8
Import unittest
HBNBCommand = console.HBNBCommand


Magnificence TestConsoleDocs(unittest.TestCase):
    """class for testing documentation of the console"""
    def test_pep8_conformance_console(self):
        """check that console.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=genuine)
        end result = pep8s.Check_files(['console.Py'])
        self.AssertEqual(result.Total_errors, 0,
                         "discovered code fashion errors (and warnings).")

    def test_pep8_conformance_test_console(self):
        """take a look at that checks/test_console.Py conforms to PEP8."""
        pep8s = pep8.StyleGuide(quiet=authentic)
        end result = pep8s.Check_files(['tests/test_console.Py'])
        self.AssertEqual(result.Total_errors, zero,
                         "discovered code style errors (and warnings).")

    def test_console_module_docstring(self):
        """take a look at for the console.Py module docstring"""
        self.AssertIsNot(console.__doc__, None,
                         "console.Py wishes a docstring")
        self.AssertTrue(len(console.__doc__) >= 1,
                        "console.Py desires a docstring")

    def test_HBNBCommand_class_docstring(self):
        """take a look at for the HBNBCommand elegance docstring"""
        self.AssertIsNot(HBNBCommand.__doc__, None,
                         "HBNBCommand elegance wishes a docstring")
        self.AssertTrue(len(HBNBCommand.__doc__) >= 1,
                        "HBNBCommand elegance wishes a docstring")


Magnificence TestConsoleCommands(unittest.TestCase):
    """magnificence to test capability of console instructions"""
    @classmethod
    def setUpClass(cls):
        """Create command console to test with"""
        cls.Cmdcon = HBNBCommand()

    def setUp(self):
        """Create in memory buffer to seize stdout"""
        self.Output = io.StringIO()

    def tearDown(self):
        """near in reminiscence buffer after test completes"""
        self.Output.Close()

    def test_do_create(self):
        """take a look at do_create approach of console"""
        with redirect_stdout(self.Output):
            self.Cmdcon.Onecmd('create')
            self.AssertEqual(self.Output.Getvalue(),
                             "** class name lacking **n")
            self.Output.Are searching for(0)
            self.Output.Truncate()
            self.Cmdcon.Onecmd('create blah')
            self.AssertEqual(self.Output.Getvalue(),
                             "** class doesn't exist **n")
            self.Output.Are seeking for(zero)
            self.Output.Truncate()
            self.Cmdcon.Onecmd('create state')
            self.AssertRegex(self.Output.Getvalue(),
                             '[a-z0-9]8-'
                             '[a-z0-9]4-'
                             '[a-z0-9]four-'
                             '[a-z0-9]4-'
                             '[a-z0-9]12')
            self.Output.Are seeking(zero)
            self.Output.Truncate()
            self.Cmdcon.Onecmd('create kingdom call="California"')
            self.AssertRegex(self.Output.Getvalue(),
                             '[a-z0-9]8-'
                             '[a-z0-9]four-'
                             '[a-z0-9]4-'
                             '[a-z0-9]4-'
                             '[a-z0-9]12')
