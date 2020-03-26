import os
import re


class FileParse:

    def __init__(self, filename):
        self.fname = filename

    def get_fname_abspath(self):
        return os.path.abspath(self.fname)

    def parse(self):
        with open(self.fname, 'r') as file:
            stri = file.read().replace('\n', '')
        return stri

    def get_line(self, n):
        fp = open(self.fname)
        for i, line in enumerate(fp):
            if i == n:
                return line
        fp.close()

    def get_numbers_in_line(self, n):
        line = self.get_line(n)
        num = re.findall(r'\d+', line)
        return num
