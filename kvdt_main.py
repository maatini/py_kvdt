#  -*- coding=iso-8859-15  -*-

__author__ = 'Martin'

import re

import kvdt_reader
import kvdt_feld_stm
from kvdt_satzarten import *
from my_token import Token


def check_kvdt_felder(tokens):
    """
    Prüfung der Feldinhalte gegen die Felddefinition
    Parameter tokens ist iterierbar und

    """
    err_cnt = 0
    for t in tokens:
        res, err_msg = kvdt_feld_stm.check_feldkennung(t.type, t.attr)
        if not res:
            print t.type, t.attr, "->",  err_msg
            err_cnt += 1

    if err_cnt > 0: print "\n\nAufgetretene Fehler:", err_cnt


class Lexer:
    def __init__(self, sequence):
        self.sequence = sequence
        self.len = len(sequence)
        self.pos = 0

    def value(self):
        v = self.sequence[self.pos] if self.pos < self.len else Token(None, '')
        return v

    def advance(self, n = 1):
        self.pos += n
        return self.pos < self.len

    def valid(self):
        return self.pos < self.len


def parse_struktur(lexer, struktur):
    """
        Einfacher Parser
        Unterstrukturen werden mittels rekursiven Abstiegs behandelt
    """

    res = []
    for f in struktur:
        (fk, bezeichner, anzahl, musskann, regeln, subfelder) = f

        token = lexer.value()
        if token is None:
            # kann-Felder überlesen, falls keine Werte vorhanden sind
            if musskann == 'm':
                raise Exception('Unerwartetes Ende des Satzes')
            else:
                continue

        # bestimmte Feldkennung erwartet
        # Muss-Felder mit hinterlegter Regel werden als Kann-Felder behandelt
        if musskann == 'm' and len(regeln) == 0 and fk != token.type:
                raise Exception('parser-fehler in %s: %s erwartet, %s gefunden' % (struktur[0][BEZEICHNER], fk, token.type))

        # solange passende Werte vorhanden sind und die erlaubte Anzahl des Vorkommens nicht überschritten ist,
        # lese Werte zum aktuellen Strukturelement
        while fk == token.type and anzahl != 0:
            anzahl -= 1

            # Ergebnis des Parsens aktualisieren
            res.append((token.type, token.attr))

            if not lexer.advance(): break
            token = lexer.value()

            # ggf. rekursiver Aufruf um Unterstruktur zu parsen
            if len(subfelder) > 0:
                res.append(parse_struktur(lexer, subfelder))
                token = lexer.value()

    return res


def parse(saetze):
    # allgemeiner Paket-Aufbau
    # con0 besa [rvsa] adt0 {010?} adt9 kadt0 {0109} kadt9 sadt0 {sad?} sadt9 con9

    # konkrerter ADT-Paket-Aufbau
    # con0 besa rvsa adt0 {0101|0102|0103|0104} adt9 con9
    re_adt = re.compile(r'con0 besa rvsa adt0 ((0101 )|(0102 )|(0103 )|(0104 ))+\s*adt9 con9')
    s = ' '.join(map(lambda x: x[0].attr, saetze))
    print s
    if re_adt.match(s):
        print "ADT-konformes Paket"
        for s in saetze:
            # Prüfung der Feldinhalte gegen die Felddefinition
            check_kvdt_felder(s)

            # Parsen der Sätze
            lexer = Lexer(s)
            data = parse_struktur(lexer, NAME_2_STRUKTUR[s[0].attr])
            print data

            # Nicht zuordenbare/ überzählige Werte anzeigen
            # Ist ein harter Fehler!
            if lexer.valid():
                while lexer.valid():
                    print "Ueberzaehlige Werte %s/%s" % (lexer.value().type, lexer.value().attr)
                    lexer.advance()
                print
    else:
        print "nicht ADT-konformes Paket!"


def parse_demo():
    import time
    t0 = time.time()

    reader = kvdt_reader.KVDT_Reader()
    saetze = kvdt_reader.scan(r'H:\work\kvdt_filter\kvdt_data02.con')

    print len(saetze), "Sätze gelesen"

    parse(saetze)
    t1 = time.time()
    print "Zeit:", t1-t0, "Sekunden"


parse_demo()

