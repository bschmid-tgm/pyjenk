"""
Author: Bernhard Schmid
Datum: 23.01.2016
Verbesserung am: 11.02.2016

Arbeitszeit schaetzung: 2 - 3 Stunden
Gearbeitete Zeit: ca. 1 1/4 Stunden

"""

import csv

class CSV(object):
    def __init__(self, file):
        self.file = file
        self.liste = []

    def read(self, filename):
        with open(filename, 'r') as f:
            try:
                dialect = csv.Sniffer().sniff(f.read(), ['\t', ';', ',', ' ', ':', '|'])
            except:
                dialect = None
            f.seek(0)
            csvreader = csv.reader(f, dialect)

            for n in csvreader:
                self.liste.append(n)

        return self.liste

    def write(self, filename):
        with open(filename, 'w') as f:
            writer = csv.writer(f)
            writer.writerows(self.liste)
