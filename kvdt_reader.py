__author__ = 'Martin'

from my_token import Token

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
        for line in f.readlines():
            t = Token(line[3:7], line[7:-1])
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

