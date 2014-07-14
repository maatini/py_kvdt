#  -*- coding=iso-8859-15  -*-

##    PyKVDT eine schlange und flexible KVDT-Bibliothek
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
__version__ = '0.01'

import re
import types
import string

import kvdt_reader
import kvdt_feld_stm
from kvdt_satzarten import *
from kvdt_token import Token


def check_kvdt_felder(tokens):
    """
    Prüfung der Feldinhalte gegen die Felddefinition
    Parameter tokens ist iterierbar.
    Konkrete Prüfungen siehe Modul kvdt_feld_stm.
    """
    err_cnt = 0
    for t in tokens:
        res, err_msg = kvdt_feld_stm.check_feldkennung(t.type, t.attr)
        if not res:
            print t.type, t.attr, "->",  err_msg
            err_cnt += 1

    if err_cnt > 0: print "\n\nAufgetretene Fehler:", err_cnt


class Lexer:
    """
        Utility-Klasse für den Zugriff auf die Liste
        der Feldkennung/ Feldkennungswerte-Liste
    """
    # EndOfToken
    EOT = Token(None, '')

    def __init__(self, sequence):
        self.sequence = sequence
        self.len = len(sequence)
        self.pos = 0

    def value(self):
        v = self.sequence[self.pos] if self.pos < self.len else Lexer.EOT
        return v

    def advance(self, n = 1):
        self.pos += n
        return self.pos < self.len

    def valid(self):
        return self.pos < self.len

    def __repr__(self):
        return "pos:%d current:(%s, %s) seq:%s\n" % (
            self.pos,
            self.sequence[self.pos].type, self.sequence[self.pos].attr,
            ', '.join(map(lambda o:o.type+'/'+o.attr, self.sequence))
        )

def parse_struktur(lexer, struktur):
    """
        Einfacher Parser
        Unterstrukturen werden mittels rekursiven Abstiegs behandelt
    """

    res = []
    for f in struktur:
        if type(f) is list:
            (fk, bezeichner, anzahl, muss_kann, regeln, subfelder) = f[:6]
        else:
            # function ggf. muss letztes Element in Struktur sein
            return f(res)

        token = lexer.value()
        # keine weiteren Datenfelder vorhanden?
        if token == Lexer.EOT:
            # kann-Felder überlesen, falls keine Werte vorhanden sind
            if muss_kann == 'm' and len(regeln) == 0:
                raise Exception('Unerwartetes Ende des Satzes')
            else:
                continue

        # bestimmte Feldkennung erwartet
        # Muss-Felder mit hinterlegter Regel werden als Kann-Felder behandelt
        if fk != token.type and muss_kann == 'm' and len(regeln) == 0:
                raise Exception('parser-fehler in %s: %s erwartet, %s gefunden' % (struktur[0][BEZEICHNER], fk, token.type))

        # mehrfaches Vorkommen möglich?
        ist_wiederholungsfeld = anzahl != 1

        # solange passende Werte vorhanden sind und die erlaubte Anzahl des Vorkommens nicht überschritten ist,
        # lese Werte zum aktuellen Strukturelement
        res_struktur = []
        while fk == token.type and anzahl != 0:
            anzahl -= 1

            # Ergebnis des Parsens merken
            res_element = [(token.type, token.attr)]
            # Regeln prüfen
            for regel in regeln:
                if type(regel) is types.FunctionType:
                    f = regel(gKontext)
                    if not f:
                        print "Zeile %d:Lambda-Ausdruck für Feld %s nicht erfüllt!" % (token.line_nbr, fk)


            # ggf. rekursiver Aufruf um Unterstruktur zu parsen
            if lexer.advance() and len(subfelder) > 0:
                # Unterstruktur parsen
                # Abhängig von der Cardinalität (1-mal oder beliebig häufig)
                # ein Array oder ein Array von Arrays erzeugen
                # Beispiel hierzu sind Leistungen
                res_sub = parse_struktur(lexer, subfelder)
                res_element.extend(res_sub)

                if type(f[-1]) is types.FunctionType:
                    res_element = f[-1](res_element)

            token = lexer.value()

            # Ergebnis für Wiederholungsfelder ist Liste mit Elementen
            # anderenfalls das Element
            if len(res_element) > 0:
                if ist_wiederholungsfeld:
                    res_struktur.append(res_element)
                else:
                    res_struktur = res_element

        if len(res_struktur) > 0:
            if ist_wiederholungsfeld:
                res.append(res_struktur)
            else:
                res.extend(res_struktur)

    return res


def parse(saetze):
    # allgemeiner Paket-Aufbau auf Satzart-Ebene als regulärer Ausdruck
    # con0 besa [rvsa] adt0 {010?} adt9 kadt0 {0109} kadt9 sadt0 {sad?} sadt9 con9

    # konkreter ADT-Paket-Aufbau
    # con0 besa rvsa adt0 {0101|0102|0103|0104} adt9 con9
    re_adt = re.compile(r'con0 besa rvsa adt0 ((0101 )|(0102 )|(0103 )|(0104 ))+\s*adt9 con9')

    # erstelle aus den im Paket vorkommenden Satzarten einen durch ' ' separierten String
    s = ' '.join(map(lambda x: x[0].attr, saetze))
    # print s

    if re_adt.match(s):
        print "ADT-konformes Paket"
        for s in saetze:
            # Prüfung der Feldinhalte gegen die Felddefinition
            check_kvdt_felder(s)

            # Parsen der Sätze
            lexer = Lexer(s)
            global gKontext
            gKontext['Satzart'] = str(s[0])
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


def parse_demo(file_spec):
    import time
    t0 = time.time()

    saetze = kvdt_reader.scan(file_spec)
    print len(saetze), "Sätze gelesen"

    parse(saetze)

    t1 = time.time()
    delta = t1-t0
    print "Zeit %f Sekunden -> #Saetze/min:%f" % (delta, 60.0/delta*len(saetze))


import sys

msg = """
    PyKVDT  Copyright (C) 2014 martin.richardt@googlemail.com
    This program comes with ABSOLUTELY NO WARRANTY
"""

print msg

# Kontext als globales Dictionary
gKontext = {}
parse_demo(sys.argv[1] if len(sys.argv) > 1 else r'd:\work\kvdt_filter\kvdt_data02.con')

