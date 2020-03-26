import os
import re


class FileParser:

    def __init__(self, filename):
        self.fname = filename

    def get_fname_abspath(self):
        return os.path.abspath(self.fname)

    def parse(self):
        with open(self.fname, 'r') as file:
            string = file.read()
        return string

    def get_line(self, n):
        with open(self.fname, 'r') as file:
            for i, line in enumerate(file):
                if i == n:
                    return line
                    break

    def get_numbers_in_line(self, n):
        line = self.get_line(n)
        num = re.findall(r'\d+', line)
        return num
