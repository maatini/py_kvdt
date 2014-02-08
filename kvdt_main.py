#  -*- coding=iso-8859-15  -*-

__author__ = 'Martin'

import re

import kvdt_reader
import kvdt_feld_stm
from kvdt_satzarten import *
from my_token import Token


def check_kvdt_felder(tokens):
    err_cnt = 0
    for t in tokens:

        if t.type == '8000':
            print "*********************satzart", t.attr

        res, err_msg = kvdt_feld_stm.check_feldkennung(t)
        if not res:
            print t, err_msg
            err_cnt += 1

        else:
            info = kvdt_feld_stm.ALLE_FELDKENNUNGEN[t.type]
            print "%s: >%s<" % (info[0],t.attr)

    print "\n\nAufgetretene Fehler:", err_cnt


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
    # FK, BEZEICHNER, ANZAHL, MUSSKANN, REGELN, SUBFELDER
    res = []
    for f in struktur:
        (fk, bezeichner, anzahl, musskann, regeln, subfelder) = f

        v = lexer.value()
        if v is None:
            if  musskann == 'm':
                raise Exception('Unerwartetes Ende des Satzes')
            else:
                continue

        # bestimmte erwartet
        if musskann == 'm' and len(regeln) == 0 and fk != v.type:
                raise Exception('parser-fehler in %s: %s erwartet, %s gefunden' % (struktur[0][BEZEICHNER], fk, v.type))

        while fk == v.type and anzahl != 0:
            anzahl -= 1

            res.append((v.type, v.attr))
            if not lexer.advance():
                break
            v = lexer.value()
            if len(subfelder) > 0:
                res.append(parse_struktur(lexer, subfelder))
                v = lexer.value()

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
            print s[0].attr
            print parse_struktur(Lexer(s), NAME_2_STRUKTUR[s[0].attr])
    else:
        print "nicht ADT-konformes Paket!"


def parse_demo():
    reader = kvdt_reader.KVDT_Reader()
    saetze = kvdt_reader.scan(r'H:\work\kvdt_filter\kvdt_data02.con')

    #check_kvdt_felder(tokens)
    print len(saetze), "Sätze gelesen"

    parse(saetze)



parse_demo()

