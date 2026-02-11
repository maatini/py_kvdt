#  -*- coding=iso-8859-15  -*-
##    PyKVDT ein schlange und flexible KVDT-Bibliothek
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


def process_lanr9(data):
    """
        ["0212", "LANR", -1, "m",  [], [
            ["0219", "Titel", 1, "k",  [], []],
            ["0220", "Arztvorname", 1, "k",  [], []],
            ["0221", "Namenszusatz", 1, "k",  [], []],
            ["0211", "Arztname", 1, "m",  ["R719"], []],
            process_lanr9
        ]]
    ]
    """

    return {'Arztname':data[-1][1], 'LANR9': data[0][1]}


def process_con0(data):
    """
    ["8000", "con0", 1, "m",  [], []],
    ["9103", "Erstellungsdatum", 1, "m",  [], []],
    ["9106", "Zeichensatz", 1, "m",  [], [
        ["9132", "Datenpakete", -1, "m",  [], []]],
    process_con0
    ]
    """
    datum = data[1][1]
    return {
        "Erstellungsdatum": "%s.%s.%s" %(datum[0:2], datum[2:4], datum[4:]),
        "Zeichensatz" : data[2][0][1]
    }


def process_leistung(data):
    """
        ["5001", "GNR", -1, "m",  [], [
            ["5002", "Art_der_Untersuchung", 1, "k",  [], []],
            ["5005", "Multiplikator", 1, "k",  [], []],
            ["5006", "Um_Uhrzeit", 1, "k",  [], []],
            ["5008", "DKM", 1, "k",  [], []],
            ["5009", "Begründungstext", -1, "k",  [], []],
            ["5012", "Sachkosten", -1, "k",  [], [
                ["5011", "Sachkosten_Bezeichnung", -1, "m",  [], []]]
            ],

            ["5013", "Prozent_der_Leistung", 1, "k",  [], []],
            ["5015", "Organ", -1, "k",  [], []],
            ["5016", "Name_des_Arztes", -1, "k",  [], []],
            ["5017", "Besuchsort", 1, "k",  [], []],
            ["5018", "Zone", 1, "k",  [], []],
            ["5019", "Erbringungsort", 1, "k",  [], []],
            ["5020", "Wiederholungsuntersuchung", 1, "k",  [], [
                ["5021", "Jahr_der_letzten_Krebsfrüherkennungsuntersuchung", 1, "k",  [], []]]
            ],
            ["5023", "GO_Nummern_Zusatz", 1, "k",  [], []],
            ["5024", "GNR_Zusatzkennzeichen", 1, "k",  [], []],
            ["5025", "Aufnahmedatum", 1, "k",  [], []],
            ["5026", "Entlassungsdatum", 1, "k",  [], []],
            ["5034", "OP-Datum", 1, "k",  [], []],
            ["5035", "OP-Schlüssel", -1, "k",  [], [
                ["5041", "Seitenlokalisation_OPS", 1, "k",  [], []]]
            ],
            ["5036", "GNR_als_Begründung", -1, "k",  [], []],
            ["5037", "Simultaneingriff", 1, "m",  ["Simultaneingriff"], []],
            ["5038", "Komplikation", -1, "k",  [], []],
            ["5040", "Patientennummer", 1, "k",  [], []],
            ["5042", "Mengenangabe", 1, "k",  [], [
                ["5043", "Maßeinheit", 1, "m",  [], []]]
            ],
            ["5070", "OMIM_G_KODE", 1, "m",  ["R770"], []],
            ["5071", "OMIM_P_KODE", 1, "m",  ["R770"], [
                ["5072", "Gen_Name", -1, "m",  ["R772"], []],
                ["5073", "Art_der_Erkrankung", -1, "m",  ["R773"], []]]
            ],
            ["5098", "BSNR", 1, "m",  [], []],
            ["5099", "LANR", 1, "m",  [], []],
            kvdt_processing.process_leistung
    """
    return "%s/%s/%s" % (data[0][1], data[-1][1], data[-2][1])


