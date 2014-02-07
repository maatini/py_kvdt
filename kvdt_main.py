__author__ = 'Martin'


import kvdt_reader
import kvdt_feld_stm

def check_kvdt_felder(reader):
    err_cnt = 0
    for t in reader.tuples():

        if t[0] == '8000':
            print "*********************satzart", t[1]

        res, err_msg = kvdt_feld_stm.check_feldkennung(t)
        if not res:
            print t, err_msg
            err_cnt += 1

        else:
            info = kvdt_feld_stm.ALLE_FELDKENNUNGEN[t[0]]
            print "%s: >%s<" % (info[0], t[1])

    print "\n\nAufgetretene Fehler:", err_cnt


reader = kvdt_reader.KVDT_Reader(r'H:\work\kvdt_filter\Z05123456699_30.06.2013_12.00.CON')
check_kvdt_felder(reader)

print len(reader.tuples()), "Felder gelesen"

