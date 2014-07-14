##    PyKVDT ein schlange und flexible KVDT-Bibliothek
##    Copyright (C) 2014  martin.richardt@googlemail.com
##
##    This program is free software: you can redistribute it and/or modify
##    it under the terms of the GNU General Public License as published by
##    the Free Software Foundation, either version 3 of the License, or
##    (at your option) any later version.
##
##    This program is distributed in the hope that it will be useful,
##    but WITHOUT ANY WARRANTY; without even the implied warranty of
##    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
##    GNU General Public License for more details.
##
##    You should have received a copy of the GNU General Public License
##    along with this program.  If not, see <http://www.gnu.org/licenses/>.


__author__ = 'Martin'

from kvdt_token import Token

class KVDT_Reader:
    """
    Liest den Inhalt einer KVDT-Datei und erzeugt daraus eine Liste
    von Token
    """

    def __init__(self):
        self.saetze = []

    def tokenize(self, filespec):
        f = open(filespec, "r")
        satz = []
        for line_nbr, line in enumerate(f.readlines()):
            t = Token(line[3:7], line[7:-1], line_nbr+1)
            if t.type == "8000":
                if len(satz) > 0:
                    self.saetze.append(satz[:])
                    satz = []
            satz.append(t)
        self.saetze.append(satz[:])

        f.close()
        return self.saetze


def scan(filespec):
    scanner = KVDT_Reader()
    return scanner.tokenize(filespec)

