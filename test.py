import os
import unittest
from trainig import FileParser


class TestFileParser(unittest.TestCase):

    x = FileParser("setup.py")

    def test_fname(self, x=x):
        # Test if the saved filename is correct
        in_file = "setup.py"

        self.assertEqual(x.fname, in_file)

    def test_abspath(self, x=x):
        # Test if the generated absolute path is correct
        file_path = os.path.abspath("setup.py")

        self.assertEqual(x.get_fname_abspath(), file_path)

    def test_parse(self, x=x):
        # Test if the content is right
        with open("setup.py", 'r') as file:
            string = file.read()

        self.assertEqual(x.parse(), string)

    def test_line(self, x=x):
        # Test if the selected line is right
        line = "    python_requires='>=3.6, <3.8',\n"

        self.assertEqual(x.get_line(28), line)

    def test_numbers_in_line(self, x=x):
        # Test if the retrieved numbers are right
        numbers = ['3', '6', '3', '8']

        self.assertEqual(x.get_numbers_in_line(28), numbers)


if __name__ == "__main__":
    unittest.main()
