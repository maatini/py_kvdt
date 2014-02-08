#  -*- coding=iso-8859-15  -*-

__author__ = 'Martin'

import re

import kvdt_reader
import kvdt_feld_stm
from kvdt_satzarten import *


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
        return self.sequence[self.pos] if self.pos <self.len else None

    def advance(self, n = 1):
        self.pos += n
        print self.sequence[self.pos].type if self.pos < self.len else 'EOF'
        return self.pos < self.len

    def valid(self):
        return self.pos < self.len


def parse_struktur(lexer, struktur):
    # FK, BEZEICHNER, ANZAHL, MUSSKANN, REGELN, SUBFELDER

    for f in struktur:
        v = lexer.value()

        # bestimmte erwartet
        if f[MUSSKANN] == 'm' and len(f[REGELN]) == 0 and f[FK] != v.type:
                raise Exception('parser-fehler in %s: %s erwartet, %s gefunden' % (struktur[0][BEZEICHNER], f[FK], v.type))

        n = f[ANZAHL]
        while f[FK] == v.type and n != 0:
            n -= 1
            if not lexer.advance():
                break

            if len(f[SUBFELDER]) > 0:
                parse_struktur(lexer, f[SUBFELDER])

        i += 1
        if not lexer.valid():
            break

    # alle Wert-Felder im Satz in Struktur ge-'parsed'
    # nicht ge-'parsed' Strukturfelder müssen optional sein,
    # damit es passt

    while i < len(struktur) and struktur[i][MUSSKANN] == 'k':
        i += 1
    print
    return i >= len(struktur)


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
            parse_struktur(Lexer(s), NAME_2_STRUKTUR[s[0].attr])
    else:
        print "nicht ADT-konformes Paket!"


def parse_demo():
    reader = kvdt_reader.KVDT_Reader()
    saetze = kvdt_reader.scan(r'H:\work\kvdt_filter\kvdt_data02.con')

    #check_kvdt_felder(tokens)
    print len(saetze), "Sätze gelesen"

    parse(saetze)



parse_demo()

