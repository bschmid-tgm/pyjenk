"""
Author: Bernhard Schmid
Verbesserung am: 12.02.2016

Arbeitszeit schaetzung: 1ne Stunden
Gearbeitete Zeit: ca. 1/2 Stunden
"""

import unittest
from Main import *

class TestAllgemein(unittest.TestCase):

    def setUp(self):
        self.csvfile = CSV("test.csv")
        pass

    def test_csvFile(self):
        self.csvfile.read("test_3.csv")
        self.csvfile.write("test.csv")

    def test_dialects(self):
        self.csvfile.read("Test-Dialects.csv")
        self.csvfile.write("test_2.csv")

    def test_noneDialect(self):
        self.csvfile.read("test.txt")
        self.csvfile.write("test_2.csv")

if __name__ == "__main__":
    unittest.main()
