#  -*- coding=iso-8859-15  -*-

__author__ = 'Martin'


import kvdt_reader
import kvdt_feld_stm



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


def parse(tokens):
    current = 0

    def match(fk, attr=None):
        return fk == tokens[current].type and (attr is None or attr == tokens[current].attr)

    def match_or_except(fk, attr=None):
        if not(fk == tokens[current].type and (attr is None or attr == tokens[current].attr)):
            raise Exception('%s/%s erwartet:%s' %(fk, '' if attr is None else attr, tokens[current]))

    def read_con0(current):
        match_or_except('9103'); current += 1
        match_or_except('9106'); current += 1
        match_or_except('9132'); current += 1
        while match('9132'):
            current += 1

        return current

    def read_besa(current):
        # (N)BSNR
        match_or_except('0201')
        while match('0201'):
            current += 1
            # (N)BSNR-Bezeichnung
            match_or_except('0203')
            current += 1
            # LANR
            match_or_except('0212')
            while match('0212'):
                current += 1
                # Titel des Arztes
                if match('0219'): current += 1
                # Arztvorname
                if match('0220'): current += 1
                # Namenszusatz des Arztes
                if match('0221'): current += 1
                # Arztname oder Erläuterung
                if match('0211'): current += 1

            # Straße der (N)BSNR-Adresse
            match_or_except('0205'); current += 1
            # PLZ der (N)BSNR-Adresse
            match_or_except('0215'); current += 1
            # Ort der (N)BSNR-Adresse
            match_or_except('0216'); current += 1
            # Telefonnummer
            match_or_except('0208'); current += 1
            # Telefaxnummer
            if match('0209'): current += 1
            # E-Mail der (N)BSNR /Praxis
            if match('0218'): current += 1
        return current

    def rvsa(current):
        match_or_except('0201')
        while match('0201'):
            current += 1
            match_or_except('0300')

            match_or_except('0301')
            while match('0302'):
                current += 1
                match_or_except('0303')

            while match('0304'):
                current += 1
                match_or_except('0305')





    match_or_except('8000', 'con0')
    current += 1

    # BESA
    if match('0201'):
        while match('0201'):
            current = read_besa(current+1)

    # RVSA
    if tokens[current].match('8000', 'rvsa'):
        current = read_rvsa(current+1)

    # ADT
    if tokens[current].match('8000', 'adt0'):
        current = read_adt0(current)
        while tokens[current].match('8000') and tokens[current].attr in ['0101', '0102', '0103', '0104']:
            if tokens[current].attr == '0101':
                current = parse_0101(current)
            elif tokens[current].attr == '0102':
                current = parse_0102(current)
            elif tokens[current].attr == '0103':
                current = parse_0103(current)
            else:
                current = parse_0104(current)

        if not tokens[current].match('8000', 'adt9'):
            raise Exception('8000/adt9 erwartet:'+tokens[current])

    else:
        raise Exception('8000/adt0 erwartet:'+tokens[current])


def parse_demo():
    reader = kvdt_reader.KVDT_Reader()
    tokens = kvdt_reader.scan(r'H:\work\kvdt_filter\Z05123456699_30.06.2013_12.00.CON')

    check_kvdt_felder(tokens)
    print len(tokens), "Felder gelesen"

    parse(tokens)

from satz_stm import KVDT_Stamm

DIRPATH = r'H:\work\kvdt_filter\src\satzarten'
stm = KVDT_Stamm(DIRPATH)

