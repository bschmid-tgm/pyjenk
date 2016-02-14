"""
Author: Bernhard Schmid
Datum: 23.01.2016

Arbeitszeit schaetzung: 2 - 3 Stunden
Gearbeitete Zeit: ca. 2 Stunden

Methoden Aufgaben:
    ReadWienWahlen: Einlesen eines CSV-Files (unterschiedlicher Dialekt) in den Hauptspeicher
    AddToWienWahlen: Einlesen eines CSV-Files (unterschiedlicher Dialekt) und an vorhandene Daten im Hauptspeicher anhängen
    WriteWienWahlen: Ausgeben von eingelesen Daten in ein CSV-File (unterschiedliche Dialekte)
    PrintWienWahlen: (war nicht geforder) Inhalt eines CSV-Files in der Console anzeigen lassen.
"""

import csv

class CSV(object):
    def ReadWienWahlen(self):
        """

        ReadWienWahlen(), liest die Daten aus einem .csv - File in den "Hauptspeicher" ein
        Die default "Lese-Optionen" sind r & rt
        Nicht jedes CSV-File ist gleich, um zu garantieren, dass die Methode mit allen CSV-Files funktioniert
        wird der "Dialekt" des Files bestimmt

        Aufgabe dieser Methode:
        Einlesen eines CSV-Files (unterschiedlicher Dialekt) in den Hauptspeicher

        :return:
        """
        csvfile = open( "Gemeinderatswahlen_(Sprengl).csv", "rt" )

        try:
            # Herausfinden & definieren, welchen Dialekt das CSV-File besitzt
            dialect = csv.get_dialect
            #Einlesen des CSV-Files aufgrund dessen Dialekts
            reader = csv.reader( csvfile, dialect )
            # CSV-File-Daten in den Hauptsepicher einlesen
            data = [row for row in reader]

            #for row in data:
                #print(row)

        finally:
            csvfile.close()

    def AddToWienWahlen(self):
        """

        Diese Methode fuegt an den Inhalt des "Hauptspeichers" den Inhalt eines anderen CSV-FIles an. Die aufgabe war weitere Daten an ein vorhandenes CSV-File
        bzw. Daten im Hauptspeicher an zu haengen. Allerdings wuerde es mehr Zeit in anspruch nehmen einen neuen Datensatz zu definieren als einfach eine Zeile in einem CSV-File zu schreiben.

        Es ist eigentlich das selbe Prinzip wie in der Methode ReadWienWahlen. Einziger zusatz ist das wir die Daten aus zwei CSV-Files auslesen und
        in den Hauptspeicher laden. Das erste File ist im "Hauptspeicher" und wir haengen das zweite dran
        (um zu ueberpruefen ob dies funktioniert hat kann man die Daten anzeigen lassen)

        Aufgabe der Methode:
        Einlesen eines CSV-Files (unterschiedlicher Dialekt) und an vorhandene Daten im Hauptspeicher anhängen

        :return:
        """
        csvfile = open( "Gemeinderatswahlen_(Sprengl).csv", "rt" )
        csvfile2 = open( "append_to_Gemeinderatswahlen_(Sprengl).csv", "rt" )
        try:
            # Herausfinden, welchen Dialekt das CSV-File besitzt
            dialect = csv.get_dialect
            #Einlesen des CSV-Files aufgrind dessen Dialekts
            reader1 = csv.reader( csvfile, dialect )
            reader2 = csv.reader( csvfile2, dialect )
            # CSV-File-Daten in den Hauptsepicher einlesen
            data1 = [row for row in reader1]
            data2 = [row for row in reader2]

            data = data1 + data2

            #Ausgeben der Daten zum Testen
            #for row in data:
                #print(row)

        finally:
            csvfile.close()

    def WriteWienWahlen(self):
        """

        WriteWienWahlen, ist ein bisschen Kontrovers. Die Methode basiert auf dem Kopieren des Inhaltes des Gemeinderatswahlen_(Sprengl).csv - Files in ein neues File
        Die Aufgabe war ein CSV-FIle zu erstellen. Nun, nichts anderes macht diese Methode. Wir definieren die Daten (Zeilen und Spalten) nicht slebst sondern Lesen sie
        aus dem schon vorhandenen CSV-File aus und schreiben diese in da neue CSV-File hinein.
        Als letztes geben wir den Inhalt des neuen CSV-Files in der Console aus.

        Aufgabe dieser Methode:
        Ausgeben von eingelesen Daten in ein CSV-File (unterschiedliche Dialekte)

        :return:
        """
        try:
            with open('Gemeinderatswahlen_(Sprengl).csv', 'r') as read_csvfile, \
                 open('New_Gemeinderatswahlen_(Sprengl).csv', 'w') as write_csvfile, \
                 open('New_Gemeinderatswahlen_(Sprengl).csv', 'r') as reed_new_csvfile:

                dialect = csv.get_dialect
                wwo = csv.reader(read_csvfile, dialect)
                #Um einen leeren Eintrag zwischen jeder Zeile zu vermeiden, muss man den "lineterminator"-Parameter definieren
                #linetreminator: The string used to terminate lines produced by the writer. It defaults to '\r\n'.
                www = csv.writer(write_csvfile, dialect,lineterminator = '\n')
                rnww = csv.reader(reed_new_csvfile,dialect)

                for row in wwo:
                    www.writerow(row)

                data = [row for row in rnww]
                print('')
                print('Wien Wahlen (Sprengl) NEU')
                print('')
                for row in data:
                    print(row)
        finally:
            read_csvfile.close()
            write_csvfile.close()

    def PrintWienWahlen(self):
        """

        Alle Zeilen und Spalten vom CSV-File in der Console anzeigen lassen (Print)

        Diese Methode war eig. nicht geforder....

        :return:
        """
        csvfile = open( "Gemeinderatswahlen_(Sprengl).csv", "r" )

        try:
            # Herausfinden, welchen Dialekt das CSV-File besitzt
            dialect = csv.get_dialect
            #Einlesen des CSV-Files aufgrind dessen Dialekts
            reader = csv.reader( csvfile, dialect )
            # CSV-File-Daten in den Hauptsepicher einlesen
            data = [row for row in reader]
            #CSV-File-Print
            print('')
            print('Wien Wahlen (Sprengl)')
            print('')
            # Ausgeben aller Zeilen im CSV-File
            for row in data:
                print(row)
        finally:
            csvfile.close()

    #Ausfuehern der Methoden
    ReadWienWahlen()
    AddToWienWahlen()
    #PrintWienWahlen()
    WriteWienWahlen()
    print()
    print('Um anzuzeigen was sich aendert entfernen Sie die Rauten bei den Forschleifen die zum anzeigen der Daten verantwortlich sind')