__author__ = 'Martin'

from my_token import Token

class KVDT_Reader:
    """
    Liest den Inhalt einer KVDT-Datei und erzeugt daraus eine Liste
    von Token
    """

    def __init__(self):
        self.tokens_ = []

    def tokenize(self, filespec):
        f = open(filespec, "r")
        for line in f.readlines():
            self.tokens_.append(Token(line[3:7], line[7:-1]))
        f.close()
        return self.tokens_


def scan(filespec):
    scanner = KVDT_Reader()
    return scanner.tokenize(filespec)

