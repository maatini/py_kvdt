#  -*- coding=iso-8859-15  -*-

import os
import re

re_comment = re.compile(r'^#.*')
re_empty_line = re.compile(r"^\s*$")
re_data = re.compile(r'^(\d{4})([ ]+.)\s+(\w)\s+(.+)$')

class KVDT_Satzdefinition:
    def __init__(self, dirpath, filename):
        self.dirpath = dirpath
        self.filename = filename
        self.art = filename.split('.')[0]
        self.lese_struktur()

    def lese_struktur(self):
        file_spec = os.path.join(self.dirpath, self.filename)
        for line in file(file_spec):
            if re_comment.match(line) or re_empty_line.match(line):
                continue

            m = re_data.match(line)
            if m:
                fk = m.group(1)
                s = m.group(2)
                level = (len(s)-1)/2
                card = s[-1]
                art = m.group(3)
                regeln = m.group(4).split() # Regeln* Bezeichnung
                feldname = regeln.pop()

                print "%s %-16s %s %s %s %s" % (fk, feldname, level, card, art, regeln)
            else:
                raise Exception("unerwartete Zeile %s in %s" % (line, file_spec))



class KVDT_Stamm:
    def __init__(self, dirpath):
        self.dirpath = dirpath
        self.saetze = self.lese_saetze()

    def lese_saetze(self):
        files = os.listdir(self.dirpath)
        res = []
        for f in files:
            print "lese Satzart:", f
            res.append(KVDT_Satzdefinition(self.dirpath, f))
            print "\n\n"
        return res



