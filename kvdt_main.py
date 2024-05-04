# -*- coding: utf-8 -*-

##    PyKVDT a snake and flexible KVDT library
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

import kvdt_reader
import kvdt_feld_stm
from kvdt_satzarten import *
from kvdt_token import Token


def check_kvdt_felder(tokens):
    """
    Check field contents against the field definition
    Parameter tokens is iterable.
    See the kvdt_feld_stm module for specific checks.
    """
    err_cnt = 0
    for t in tokens:
        res, err_msg = kvdt_feld_stm.check_feldkennung(t.type, t.attr)
        if not res:
            print(t.type, t.attr, "->", err_msg)
            err_cnt += 1

    if err_cnt > 0:
        print("\n\nErrors occurred:", err_cnt)


class Lexer:
    """
        Utility class for accessing the list
        of field identifications/ field value lists
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

    def advance(self, n=1):
        self.pos += n
        return self.pos < self.len

    def valid(self):
        return self.pos < self.len

    def __repr__(self):
        return "pos:%d current:(%s, %s) seq:%s\n" % (
            self.pos,
            self.sequence[self.pos].type, self.sequence[self.pos].attr,
            ', '.join(map(lambda o: o.type + '/' + o.attr, self.sequence))
        )


def parse_struktur(lexer, struktur):
    """
        Simple parser
        Substructures are treated via recursive descent
    """

    res = []
    for f in struktur:
        if isinstance(f, list):
            (fk, bezeichner, anzahl, muss_kann, regeln, subfelder) = f[:6]
        else:
            # function possibly last element in structure
            return f(res)

        token = lexer.value()
        # no further data fields present?
        if token == Lexer.EOT:
            # skip optional fields if no values are present
            if muss_kann == 'm' and len(regeln) == 0:
                raise Exception('Unexpected end of the sentence')
            else:
                continue

        # specific field identification expected
        # Must fields with a defined rule
        # are treated as optional fields
        if fk != token.type and muss_kann == 'm' and len(regeln) == 0:
            raise Exception('parser error in %s: %s expected, %s found' % (struktur[0][BEZEICHNER], fk, token.type))

        # multiple occurrences possible?
        is_repeating_field = anzahl != 1

        # as long as matching values are present and the allowed occurrence count is not exceeded,
        # read values to the current structural element
        res_struktur = []
        while fk == token.type and anzahl != 0:
            anzahl -= 1

            # Remember the parsing result
            res_element = [(token.type, token.attr)]
            # Check rules
            for regel in regeln:
                if isinstance(regel, types.FunctionType):
                    f = regel(gKontext)
                    if not f:
                        print("Line %d: Lambda expression for field %s not satisfied!" % (token.line_nbr, fk))

            # possibly recursive call to parse substructure
            if lexer.advance() and len(subfelder) > 0:
                # Parse substructure
                # Depending on the cardinality (once or arbitrarily often)
                # create an array or an array of arrays
                # Example are benefits
                res_sub = parse_struktur(lexer, subfelder)
                res_element.extend(res_sub)

                if isinstance(f[-1], types.FunctionType):
                    res_element = f[-1](res_element)

            token = lexer.value()

            # The result for repeating fields is a list with elements
            # otherwise the element
            if len(res_element) > 0:
                if is_repeating_field:
                    res_struktur.append(res_element)
                else:
                    res_struktur = res_element

        if len(res_struktur) > 0:
            if is_repeating_field:
                res.append(res_struktur)
            else:
                res.extend(res_struktur)

    return res


def parse(saetze):
    # general package structure at the sentence type level as a regular expression
    # con0 besa [rvsa] adt0 {010?} adt9 kadt0 {0109} kadt9 sadt0 {sad?} sadt9 con9

    # specific ADT package structure
    # con0 besa rvsa adt0 {0101|0102|0103|0104} adt9 con9
    re_adt = re.compile(r'con0 besa rvsa adt0 ((0101 )|(0102 )|(0103 )|(0104 ))+\s*adt9 con9')

    # create a space-separated string from the sentence types occurring in the package
    s = ' '.join(map(lambda x: x[0].attr, saetze))
    print(s)

    if re_adt.match(s):
        print("ADT-compliant package")
        for s in saetze:
            # Check field contents against the field definition
            check_kvdt_felder(s)

            # Parse the sentences
            lexer = Lexer(s)
            global gKontext
            gKontext['Satzart'] = str(s[0])
            data = parse_struktur(lexer, NAME_2_STRUKTUR[s[0].attr])
            print(data)

            # Display non-assignable/ excess values
            # This is a serious error!
            if lexer.valid():
                while lexer.valid():
                    print("Excess values %s/%s" % (lexer.value().type, lexer.value().attr))
                    lexer.advance()
                print()
    else:
        print("Not an ADT-compliant package!")


def parse_demo(file_spec):
    import time
    t0 = time.time()

    saetze = kvdt_reader.scan(file_spec)
    print(len(saetze), "Sentences read")

    parse(saetze)

    t1 = time.time()
    delta = t1 - t0
    print("Time %f seconds -> #Sentences/min:%f" % (delta, 60.0 / delta * len(saetze)))


import sys

msg = """
    PyKVDT  Copyright (C) 2014 martin.richardt@googlemail.com
    This program comes with ABSOLUTELY NO WARRANTY
"""

print(msg)

# Context as a global dictionary
gKontext = {}
parse_demo(sys.argv[1] if len(sys.argv) > 1 else r'./Z05123456699_27.01.2024_12.00.con')
