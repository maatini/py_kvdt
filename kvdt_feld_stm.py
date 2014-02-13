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

import string

__author__ = 'Martin'

"""
Liste alle Feldkennungen mit den Attributen
    Feldbezeichnung, Länge, Typ, Erläuterung
    Struktur aus KVDT-Beschreibung übernommen.
    Aufbau:
        Feldkennung -> (Feldbeschreibung, Type-Info)

    Type-Info:
        min_len, max_len, 'a'   : alphanumerisch mit Länge im Bereich [min, max]
        'd'                     : Datum, Längenangaben optional
        'g'                     : GOP
        min_len, max_len, 'n'   : numerisch mit Länge im Bereich [min, max]
        'z'                     : Zeitraum



"""

DATUM = 'd'
GOP = 'g'
ZEITRAUM = 'z'
ALPHANUMERISCH = 'a'
NUMERISCH = 'n'


ALLE_FELDKENNUNGEN = {
'0102':  ['Softwareverantwortlicher (SV)', [0, 60, ALPHANUMERISCH]] ,
'0103':  ['Software', [0, 60, ALPHANUMERISCH]] ,
'0105':  ['KBV-Prüfnummer', [15, 17, ALPHANUMERISCH]] ,
'0111':  ['Email-Adresse des SV', [0, 60, ALPHANUMERISCH]] ,
'0121':  ['Straße des SV', [0, 60, ALPHANUMERISCH]] ,
'0122':  ['PLZ des SV', [0, 7, ALPHANUMERISCH]] ,
'0123':  ['Ort des SV', [0, 60, ALPHANUMERISCH]] ,
'0124':  ['Telefonnummer des SV', [0, 60, ALPHANUMERISCH]] ,
'0125':  ['Telefaxnummer des SV', [0, 60, ALPHANUMERISCH]] ,
'0126':  ['Regionaler Systembetreuer (SB)', [0, 60, ALPHANUMERISCH]] ,
'0127':  ['Straße des SB', [0, 60, ALPHANUMERISCH]] ,
'0128':  ['PLZ des SB', [0, 7, ALPHANUMERISCH]] ,
'0129':  ['Ort des SB', [0, 60, ALPHANUMERISCH]] ,
'0130':  ['Telefonnummer des SB', [0, 60, ALPHANUMERISCH]] ,
'0131':  ['Telefaxnummer des SB', [0, 60, ALPHANUMERISCH]] ,
'0132':  ['Release-Stand der Software', [0, 60, ALPHANUMERISCH]] ,
'0201':  ['Betriebs- (BSNR) oder Neben-betriebsstättennummer (NBSNR)', [9, 9, NUMERISCH]] ,
'0203':  ['(N)BSNR-/Praxisbezeichnung', [0, 60, ALPHANUMERISCH]] ,
'0205':  ['Straße der (N)BSNR-Adresse', [0, 60, ALPHANUMERISCH]] ,
'0208':  ['Telefonnummer', [0, 60, ALPHANUMERISCH]] ,
'0209':  ['Telefaxnummer', [0, 60, ALPHANUMERISCH]] ,
'0211':  ['Arztname/Erläuterung', [0, 60, ALPHANUMERISCH]] ,
'0212':  ['Lebenslange Arztnummer (LANR)', [9, 9, NUMERISCH]] ,
'0215':  ['PLZ der (N)BSNR-Adresse', [0, 7, ALPHANUMERISCH]] ,
'0216':  ['Ort der (N)BSNR-Adresse', [0, 60, ALPHANUMERISCH]] ,
'0218':  ['E-Mail (N)BSNR /Praxis', [0, 60, ALPHANUMERISCH]] ,
'0219':  ['Titel des Arztes', [0, 15, ALPHANUMERISCH]] ,
'0220':  ['Arztvorname', [0, 28, ALPHANUMERISCH]] ,
'0221':  ['Namenszusatz des Arztes', [0, 15, ALPHANUMERISCH]] ,
'0300':  ['Abrechnung von (zertifikats-pflichtigen) Laborleistungen', [1, 1, NUMERISCH]] ,
'0301':  ['pnSD/uu-Analysen', [1, 1, NUMERISCH]] ,
'0302':  ['Gerätetyp', [0, 60, ALPHANUMERISCH]] ,
'0303':  ['Hersteller', [0, 60, ALPHANUMERISCH]] ,
'0304':  ['Analyt-ID', [3, 3, NUMERISCH]] ,
'0305':  ['RV-Zertifikat', [1, 1, NUMERISCH]] ,
'3000':  ['Patientennummer', [0, 20, ALPHANUMERISCH]] ,
'3003':  ['Schein-ID', [0, 60, ALPHANUMERISCH]] ,
'3004':  ['Kartentyp/-generation eGK', [1, 1, NUMERISCH]] ,
'3005':  ['Kennziffer SA', [0, 26, ALPHANUMERISCH]] ,
'3006':  ['CDM9 Version', [5, 5, ALPHANUMERISCH]] ,
'3100':  ['Namenszusatz/Vorsatzwort des Patienten', [0, 15, ALPHANUMERISCH]] ,
'3101':  ['Name des Patienten', [0, 28, ALPHANUMERISCH]] ,
'3102':  ['Vorname des Patienten', [0, 28, ALPHANUMERISCH]] ,
'3103':  ['Geburtsdatum des Patienten,Ersatzwert: 00000000', [8, 8, NUMERISCH]] ,
'3104':  ['Titel des Patienten', [0, 15, ALPHANUMERISCH]] ,
'3105':  ['Versichertennummer des Patienten', [6, 12, NUMERISCH]] ,
'3107':  ['Straße des Patienten', [0, 28, ALPHANUMERISCH]] ,
'3108':  ['Versichertenart MFR', [1, 1, NUMERISCH]] ,
'3110':  ['Geschlecht des Patienten', [1, 1, NUMERISCH]] ,
'3112':  ['PLZ des Patienten', [0, 7, ALPHANUMERISCH]] ,
'3113':  ['Wohnort des Patienten', [0, 23, ALPHANUMERISCH]] ,
'3114':  ['Wohnsitzländercode', [0, 3, ALPHANUMERISCH]] ,
'3116':  ['KV-Bereich', [2, 2, NUMERISCH]] ,
'3119':  ['Versichertennummer eGK des Patienten', [10, 10, ALPHANUMERISCH]] ,
'3674':  ['Diagnosensicherheit Dauerdiagnose', [1, 1, ALPHANUMERISCH]] ,
'3675':  ['Seitenlokalisation Dauerdiagnose', [1, 1, ALPHANUMERISCH]] ,
'3676':  ['Diagnosenerläuterung Dauerdiagnose', [0, 60, ALPHANUMERISCH]] ,
'3677':  ['Diagnosenausnahmetatbestand Dauerdiagnosen', [0, 60, ALPHANUMERISCH]] ,
'4101':  ['Quartal', [5, 5, NUMERISCH]] ,
'4102':  ['Ausstellungsdatum', [DATUM]] ,
'4104':  ['Abrechnungs-VKNR', [5, 5, NUMERISCH]] ,
'4106':  ['Kostenträger-Abrechnungsbereich (KTAB)', [2, 2, NUMERISCH]] ,
'4108':  ['Zulassungsnummer (mobiles Lesegerät)', [0, 30, ALPHANUMERISCH]] ,
'4109':  ['letzter Einlesetag der Versichertenkarte im Quartal', [DATUM]] ,
'4110':  ['Bis-Datum der Gültigkeit', [4, 4, NUMERISCH]] ,
'4111':  ['Krankenkassennummer (IK)', [7, 7, NUMERISCH]] ,
'4112':  ['Versichertenstatus', [4, 4, NUMERISCH]] ,
'4113':  ['Statusergänzung/DMP-Kennzeichnung', [1, 1, ALPHANUMERISCH]] ,
'4121':  ['Gebührenordnung', [1, 1, NUMERISCH]] ,
'4122':  ['Abrechnungsgebiet', [2, 2, NUMERISCH]] ,
'4123':  ['Personenkreis / Untersuchungskategorie', [2, 2, NUMERISCH]] ,
'4124':  ['SKT-Zusatzangaben  5', [0, 60, ALPHANUMERISCH]] ,
'4125':  ['Gültigkeitszeitraum von ... bis ...', [ZEITRAUM]] ,
'4126':  ['SKT-Bemerkungen', [0, 60, ALPHANUMERISCH]] ,
'4202':  ['Unfall, Unfallfolgen', [1, 1, NUMERISCH]] ,
'4204':  ['eingeschränkter Leistungsanspruch gemäß §716 Abs. 3a SGB V', [1, 1, NUMERISCH]] ,
'4205':  ['Auftrag', [0, 60, ALPHANUMERISCH]] ,
'4206':  ['Mutmasslicher Tag der Entbindung', [DATUM]] ,
'4207':  ['Diagnose/Verdachtsdiagnose', [0, 60, ALPHANUMERISCH]] ,
'4208':  ['Befund/Medikation', [0, 60, ALPHANUMERISCH]] ,
'4209':  ['Auftrag/Diagnose/Verdacht', [0, 60, ALPHANUMERISCH]] ,
'4217':  ['(N)BSNR des Erstveranlassers', [9, 9, NUMERISCH]] ,
'4241':  ['Lebenslange Arztnummer (LANR) des Erstveranlassers Ersatzwert: 999999900', [9, 9, NUMERISCH]] ,
'4218':  ['(N)BSNR des Ücberweisers', [9, 9, NUMERISCH]] ,
'4242':  ['Lebenslange Arztnummer des Ücberweisers Ersatzwert: 999999900', [9, 9, NUMERISCH]] ,
'4219':  ['Ücberweisung von anderen Ärzten Ersatzwert: unbekannt', [0, 60, ALPHANUMERISCH]] ,
'4220':  ['Ücberweisung an Ersatzwert: kA', [0, 60, ALPHANUMERISCH], ['0102', 'sad2']] ,
'4221':  ['Kurativ / Präventiv / ESS / bei belegärztlicher Behandlung', [1, 1, NUMERISCH]] ,
'4229':  ['Ausnahmeindikation', [5, 5, NUMERISCH]] ,
'4233':  ['Stationäre Behandlung von ... bis ...', [16, 16, NUMERISCH]] ,
'4234':  ['anerkannte Psychotherapie', [1, 1, NUMERISCH]] ,
'4235':  ['Datum des Anerkennungsbescheides', [DATUM]] ,
'4239':  ['Scheinuntergruppe', [2, 2, NUMERISCH]] ,
'4243':  ['Weiterbehandelnder Arzt Ersatzwert: unbekannt', [0, 60, ALPHANUMERISCH]] ,
'4244':  ['Bewilligte Leistung  5,', [6, 6, ALPHANUMERISCH]] ,
'4245':  ['Anzahl bewilligter Leistungen', [0, 3, NUMERISCH]] ,
'4246':  ['Anzahl abgerechneter Leistungen', [0, 3, NUMERISCH]] ,
'4247':  ['Antragsdatum Anerkennungsbescheid', [DATUM]] ,
'4261':  ['Kurart', [1, 1, NUMERISCH]] ,
'4262':  ['Durchführung als Kompaktkur', [1, 1, NUMERISCH]] ,
'4263':  ['genehmigte Kurdauer in Wochen', [0, 2, NUMERISCH]] ,
'4264':  ['Anreisetag', [DATUM]] ,
'4265':  ['Abreisetag', [DATUM]] ,
'4266':  ['Kurabbruch am', [DATUM]] ,
'4267':  ['Bewilligte Kurverlängerung in Wochen', [0, 2, NUMERISCH]] ,
'4268':  ['Bewilligungsdatum Kurverlängerung', [DATUM]] ,
'4269':  ['Verhaltenspräventive Maßnahmen angeregt', [1, 1, NUMERISCH]] ,
'4270':  ['Verhaltenspräventive Maßnahmen durchgeführt', [1, 1, NUMERISCH]] ,
'4271':  ['Kompaktkur nicht möglich', [1, 1, NUMERISCH]] ,
'5000':  ['Leistungstag', [DATUM]] ,
'5002':  ['Art der Untersuchung', [0, 60, ALPHANUMERISCH]] ,
'5005':  ['Multiplikator', [2, 2, NUMERISCH]] ,
'5006':  ['Um-Uhrzeit', [4, 4, NUMERISCH]] ,
'5008':  ['DKM', [0, 3, NUMERISCH]] ,
'5009':  ['freier Begründungstext', [0, 60, ALPHANUMERISCH]] ,
'5011':  ['Sachkosten-Bezeichnung', [0, 60, ALPHANUMERISCH]] ,
'5012':  ['Sachkosten/Materialkosten in Cent', [0, 10, NUMERISCH]] ,
'5013':  ['Prozent der Leistung', [3, 3, NUMERISCH]] ,
'5015':  ['Organ', [0, 60, ALPHANUMERISCH]] ,
'5016':  ['Name des Arztes', [0, 60, ALPHANUMERISCH]] ,
'5017':  ['Besuchsort bei Hausbesuchen', [0, 60, ALPHANUMERISCH]] ,
'5018':  ['Zone bei Besuchen', [2, 2, ALPHANUMERISCH]] ,
'5019':  ['Erbringungsort/Standort des Gerätes', [0, 60, ALPHANUMERISCH]] ,
'5020':  ['Wiederholungsuntersuchung', [1, 1, NUMERISCH]] ,
'5021':  ['Jahr der letzten Krebsfrüherkennungsuntersuchung', [4, 4, NUMERISCH]] ,
'5023':  ['GO-Nummern-Zusatz', [1, 1, ALPHANUMERISCH]] ,
'5024':  ['GNR-Zusatzkennzeichen poststationär erbrachte Leistungen', [1, 1, ALPHANUMERISCH]] ,
'5025':  ['Aufnahmedatum', [DATUM]] ,
'5026':  ['Entlassungsdatum', [DATUM]] ,
'5034':  ['OP-Datum', [DATUM]] ,
'5035':  ['OP-Schlüssel', [0, 8, ALPHANUMERISCH]] ,
'5036':  ['GNR als Begründung  5,', [6, 6, ALPHANUMERISCH]] ,
'5037':  ['Gesamt-Schnitt-Naht-Zeit(Minuten)', [0, 3, NUMERISCH]] ,
'5038':  ['Komplikation', [0, 60, ALPHANUMERISCH]] ,
'5040':  ['Patientennummer (EDV) des FEK-Bogens', [0, 8, ALPHANUMERISCH]] ,
'5041':  ['Seitenlokalisation OPS', [1, 1, ALPHANUMERISCH]] ,
'5042':  ['Mengenangabe KM /AM', [0, 5, NUMERISCH]] ,
'5043':  ['Maßeinheit KM /AM', [1, 1, NUMERISCH]] ,
'5044':  ['Betriebswirtschaftlich kalkulierter Preis in Cent', [0, 6, NUMERISCH]] ,
'5070':  ['OMIM-G-Kode des untersuchten Gens Ersatzwert: 999999', [6, 6, NUMERISCH]] ,
'5071':  ['OMIM-P-Kode (Art der Erkrankung) Ersatzwert: 999999', [6, 6, NUMERISCH]] ,
'5072':  ['Gen-Name', [0, 60, ALPHANUMERISCH]] ,
'5073':  ['Art der Erkrankung', [0, 60, ALPHANUMERISCH]] ,
'5098':  ['(N)BSNR des Ortes der Leistungserbringung', [9, 9, NUMERISCH]] ,
'5099':  ['Lebenslange Arztnummer (LANR) des Leistungserbringers Ersatzwert: 999999900', [9, 9, NUMERISCH]] ,
'6003':  ['Diagnosensicherheit', [1, 1, ALPHANUMERISCH]] ,
'6004':  ['Seitenlokalisation', [1, 1, ALPHANUMERISCH]] ,
'6006':  ['Diagnosenerläuterung', [0, 60, ALPHANUMERISCH]] ,
'6008':  ['Diagnosenausnahmetatbestand', [0, 60, ALPHANUMERISCH]] ,
'8000':  ['Satzart', [4, 4, ALPHANUMERISCH]] ,
'9102':  ['Empfänger', [2, 2, NUMERISCH]] ,
'9103':  ['Erstellungsdatum', [DATUM]] ,
'9106':  ['verwendeter Zeichensatz', [1, 1, NUMERISCH]] ,
'9115':  ['Erstellungsdatum ADT-Datenpaket', [DATUM]] ,
'9116':  ['Erstellungsdatum KADT-Datenpaket', [DATUM]] ,
'9122':  ['Erstellungsdatum SADT-Datenpaket', [DATUM]] ,
'9132':  ['enthaltene Datenpakete dieser Datei', [1, 1, NUMERISCH]] ,
'9204':  ['Abrechnungsquartal', [5, 5, NUMERISCH]] ,
'9212':  ['Version der Satzbeschreibung', [0, 11, ALPHANUMERISCH]] ,
'9250':  ['AVWG-Prüfnummer der AVS', [15, 17, ALPHANUMERISCH]] ,
'9260':  ['Anzahl Teilabrechnungen', [2, 2, NUMERISCH]] ,
'9261':  ['Abrechnungsteil x von y', [2, 2, NUMERISCH]] ,
'9901':  ['Systeminterner Parameter', [0, 60, ALPHANUMERISCH]] ,

'3673':  ['Dauerdiagnose (ICD-Code)', [3, 3, 5, 6, ALPHANUMERISCH]],
'4236':  ['Abklärung somatischer Ursachen vor Aufnahme einer Psychotherapie', [1, 1, ALPHANUMERISCH]],
'5001':  ['Gebührennummer (GNR)', [5, 9, GOP]],
'6001':  ['ICD-Code Ersatzwert: UUU', [3, 3, 5, 6, ALPHANUMERISCH]]
};


def check_feldkennung(feldkennung, feldkennungswert):
    """
    Prüfungen:
        - feldkennung im Stamm enthalten
        - feldkennungswert erfüllt Längenrestriktionen
        - feldkennungswert erfüllt Bildungsvorschrift

    Prüfungen benötigen noch den letzten Feinschliff! Prinzip ist aber klar.
    """

    def check_length(type_info, v):
        if type_info[-1] == DATUM:
            return len(v) == 8
        elif type_info[-1] == ZEITRAUM:
            return len(v) == 16
        else:
            res = type_info[0] <= len(v) and len(v) <= type_info[1]
            if not res and len(type_info) > 3:
                res = type_info[2] <= len(v) and len(v) <= type_info[3]
            return res

    def check_value(type_info, v):
        res = True
        # letztes ELement des Arrays ist Typangabe (a, d, g, n)
        type = type_info[-1]
        if type == DATUM:
            #ttmmjjjj Prüfung unvollständig!
            try:
                tag = int(v[0:2])
                monat = int(v[2:4])
                jahr = int(v[4:])
                res = (tag >=1 and tag <= 31) and (monat>=1 and monat<=12) and (jahr > 1900)
            except:
                res = False

        elif type == NUMERISCH:
            res = all([c in string.digits for c in v ])
        elif type == GOP:
            # GOP
            res = all([c in string.digits for c in v[:-1]])
            res = res and (v[-1] in string.ascii_uppercase or v[-1] in string.digits)
        return res


    if not(feldkennung in ALLE_FELDKENNUNGEN):
        return False, "Feldkennung '%s' nicht im Stamm enthalten!" % feldkennung
    else:
        info = ALLE_FELDKENNUNGEN[feldkennung]
        err = ""
        if not check_length(info[1], feldkennungswert):
            err += "'%s' Laengenrestriktion nicht eingehalten!\n" % info[0]
        if  not check_value(info[1], feldkennungswert):
            err += "'%s' Wert entspricht nicht der Bildungsvorschrift!\n" % info[0]

    return len(err) == 0, err
