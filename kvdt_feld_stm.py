#  -*- coding=iso-8859-15  -*-
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

import string

__author__ = 'Martin'

"""
List all field identifiers with the attributes
    Field description, Length, Type, Explanation
    Structure adopted from KVDT description.
    Structure:
        Field identifier -> (Field description, Type information)

    Type information:
        min_len, max_len, 'a'   : alphanumeric with length in range [min, max]
        'd'                     : Date, length specifications optional
        'g'                     : GOP
        min_len, max_len, 'n'   : numeric with length in range [min, max]
        'z'                     : Period
"""

DATUM = 'd'
GOP = 'g'
ZEITRAUM = 'z'
ALPHANUMERISCH = 'a'
NUMERISCH = 'n'


ALLE_FELDKENNUNGEN = {
'0102': ["Softwareverantwortlicher (SV) / Software Manager (SV)", [0, 60, ALPHANUMERISCH]],
'0103': ["Software / Software", [0, 60, ALPHANUMERISCH]],
'0105': ["KBV-Prüfnummer / KBV Test Number", [15, 17, ALPHANUMERISCH]],
'0111': ["Email-Adresse des SV / Email Address of the SV", [0, 60, ALPHANUMERISCH]],
'0121': ["Straße des SV / Street of the SV", [0, 60, ALPHANUMERISCH]],
'0122': ["PLZ des SV / Postal Code of the SV", [0, 7, ALPHANUMERISCH]],
'0123': ["Ort des SV / City of the SV", [0, 60, ALPHANUMERISCH]],
'0124': ["Telefonnummer des SV / Telephone Number of the SV", [0, 60, ALPHANUMERISCH]],
'0125': ["Telefaxnummer des SV / Fax Number of the SV", [0, 60, ALPHANUMERISCH]],
'0126': ["Regionaler Systembetreuer (SB) / Regional System Supervisor (SB)", [0, 60, ALPHANUMERISCH]],
'0127': ["Straße des SB / Street of the SB", [0, 60, ALPHANUMERISCH]],
'0128': ["PLZ des SB / Postal Code of the SB", [0, 7, ALPHANUMERISCH]],
'0129': ["Ort des SB / City of the SB", [0, 60, ALPHANUMERISCH]],
'0130': ["Telefonnummer des SB / Telephone Number of the SB", [0, 60, ALPHANUMERISCH]],
'0131': ["Telefaxnummer des SB / Fax Number of the SB", [0, 60, ALPHANUMERISCH]],
'0132': ["Release-Stand der Software / Release Version of the Software", [0, 60, ALPHANUMERISCH]],
'0201': ["Betriebs- (BSNR) oder Nebenbetriebsstättennummer (NBSNR) / Main (BSNR) or Auxiliary Business Site Number (NBSNR)", [9, 9, NUMERISCH]],
'0203': ["(N)BSNR-/Praxisbezeichnung / (N)BSNR-/Practice Designation", [0, 60, ALPHANUMERISCH]],
'0205': ["Straße der (N)BSNR-Adresse / Street of the (N)BSNR Address", [0, 60, ALPHANUMERISCH]],
'0208': ["Telefonnummer / Telephone Number", [0, 60, ALPHANUMERISCH]],
'0209': ["Telefaxnummer / Fax Number", [0, 60, ALPHANUMERISCH]],
'0211': ["Arztname/Erläuterung / Doctor's Name/Explanation", [0, 60, ALPHANUMERISCH]],
'0212': ["Lebenslange Arztnummer (LANR) / Lifetime Doctor Number (LANR)", [9, 9, NUMERISCH]],
'0215': ["PLZ der (N)BSNR-Adresse / Postal Code of the (N)BSNR Address", [0, 7, ALPHANUMERISCH]],
'0216': ["Ort der (N)BSNR-Adresse / City of the (N)BSNR Address", [0, 60, ALPHANUMERISCH]],
'0218': ["E-Mail (N)BSNR /Praxis / Email (N)BSNR /Practice", [0, 60, ALPHANUMERISCH]],
'0219': ["Titel des Arztes / Title of the Doctor", [0, 15, ALPHANUMERISCH]],
'0220': ["Arztvorname / Doctor's First Name", [0, 28, ALPHANUMERISCH]],
'0221': ["Namenszusatz des Arztes / Additional Name of the Doctor", [0, 15, ALPHANUMERISCH]],
'0300': ["Abrechnung von (zertifikatspflichtigen) Laborleistungen / Billing of (certificate-required) Laboratory Services", [1, 1, NUMERISCH]],
'0301': ["pnSD/uu-Analysen / pnSD/uu Analyses", [1, 1, NUMERISCH]],
'0302': ["Gerätetyp / Device Type", [0, 60, ALPHANUMERISCH]],
'0303': ["Hersteller / Manufacturer", [0, 60, ALPHANUMERISCH]],
'0304': ["Analyt-ID / Analyte ID", [3, 3, NUMERISCH]],
'0305': ["RV-Zertifikat / RV Certificate", [1, 1, NUMERISCH]],
'3000': ["Patientennummer / Patient Number", [0, 20, ALPHANUMERISCH]],
'3003': ["Schein-ID / Voucher ID", [0, 60, ALPHANUMERISCH]],
'3004': ["Kartentyp/-generation eGK / Card Type/Generation eGK", [1, 1, NUMERISCH]],
'3005': ["Kennziffer SA / SA Identifier", [0, 26, ALPHANUMERISCH]],
'3006': ["CDM9 Version", [5, 5, ALPHANUMERISCH]],
'3100': ["Namenszusatz/Vorsatzwort des Patienten / Prefix/Surname of the Patient", [0, 15, ALPHANUMERISCH]],
'3101': ["Name des Patienten / Patient's Name", [0, 28, ALPHANUMERISCH]],
'3102': ["Vorname des Patienten / Patient's First Name", [0, 28, ALPHANUMERISCH]],
'3103': ["Geburtsdatum des Patienten, Ersatzwert: 00000000 / Date of Birth of the Patient, Default Value: 00000000", [8, 8, NUMERISCH]],
'3104': ["Titel des Patienten / Title of the Patient", [0, 15, ALPHANUMERISCH]],
'3105': ["Versichertennummer des Patienten / Patient's Insurance Number", [6, 12, NUMERISCH]],
'3107': ["Straße des Patienten / Street of the Patient", [0, 28, ALPHANUMERISCH]],
'3108': ["Versichertenart MFR / Insurance Type MFR", [1, 1, NUMERISCH]],
'3110': ["Geschlecht des Patienten / Gender of the Patient", [1, 1, NUMERISCH]],
'3112': ["PLZ des Patienten / Postal Code of the Patient", [0, 7, ALPHANUMERISCH]],
'3113': ["Wohnort des Patienten / Residence of the Patient", [0, 23, ALPHANUMERISCH]],
'3114': ["Wohnsitzländercode / Country Code of Residence", [0, 3, ALPHANUMERISCH]],
'3116': ["KV-Bereich / KV Area", [2, 2, NUMERISCH]],
'3119': ["Versichertennummer eGK des Patienten / eGK Insurance Number of the Patient", [10, 10, ALPHANUMERISCH]],
'3674': ["Diagnosensicherheit Dauerdiagnose / Diagnostic Certainty of Chronic Diagnosis", [1, 1, ALPHANUMERISCH]],
'3675': ["Seitenlokalisation Dauerdiagnose / Side Localization of Chronic Diagnosis", [1, 1, ALPHANUMERISCH]],
'3676': ["Diagnosenerläuterung Dauerdiagnose / Explanation of Chronic Diagnosis", [0, 60, ALPHANUMERISCH]],
'3677': ["Diagnosenausnahmetatbestand Dauerdiagnosen / Exceptional Circumstances for Chronic Diagnoses", [0, 60, ALPHANUMERISCH]],
'4101': ["Quartal / Quarter", [5, 5, NUMERISCH]],
'4102': ["Ausstellungsdatum / Date of Issue", [DATUM]],
'4104': ["Abrechnungs-VKNR / Billing VKNR", [5, 5, NUMERISCH]],
'4106': ["Kostenträger-Abrechnungsbereich (KTAB) / Cost Carrier Billing Area (KTAB)", [2, 2, NUMERISCH]],
'4108': ["Zulassungsnummer (mobiles Lesegerät) / Approval Number (mobile Reading Device)", [0, 30, ALPHANUMERISCH]],
'4109': ["letzter Einlesetag der Versichertenkarte im Quartal / Last Reading Day of the Insurance Card in the Quarter", [DATUM]],
'4110': ["Bis-Datum der Gültigkeit / Until Date of Validity", [4, 4, NUMERISCH]],
'4111': ["Krankenkassennummer (IK) / Health Insurance Number (IK)", [7, 7, NUMERISCH]],
'4112': ["Versichertenstatus / Insurance Status", [4, 4, NUMERISCH]],
'4113': ["Statusergänzung/DMP-Kennzeichnung / Status Supplement/DMP Labeling", [1, 1, ALPHANUMERISCH]],
'4121': ["Gebührenordnung / Fee Schedule", [1, 1, NUMERISCH]],
'4122': ["Abrechnungsgebiet / Billing Area", [2, 2, NUMERISCH]],
'4123': ["Personenkreis / Untersuchungskategorie / Group of Persons / Examination Category", [2, 2, NUMERISCH]],
'4124': ["SKT-Zusatzangaben 5 / SKT Additional Information 5", [0, 60, ALPHANUMERISCH]],
'4125': ["Gültigkeitszeitraum von ... bis ... / Validity Period from ... to ...", [ZEITRAUM]],
'4126': ["SKT-Bemerkungen / SKT Comments", [0, 60, ALPHANUMERISCH]],
'4202': ["Unfall, Unfallfolgen / Accident, Accident Consequences", [1, 1, NUMERISCH]],
'4204': ["eingeschränkter Leistungsanspruch gemäß §716 Abs. 3a SGB V / Limited Benefit Entitlement according to §716 Abs. 3a SGB V", [1, 1, NUMERISCH]],
'4205': ["Auftrag / Order", [0, 60, ALPHANUMERISCH]],
'4206': ["Mutmaßlicher Tag der Entbindung / Presumed Day of Delivery", [DATUM]],
'4207': ["Diagnose/Verdachtsdiagnose / Diagnosis/Suspected Diagnosis", [0, 60, ALPHANUMERISCH]],
'4208': ["Befund/Medikation / Findings/Medication", [0, 60, ALPHANUMERISCH]],
'4209': ["Auftrag/Diagnose/Verdacht / Order/Diagnosis/Suspicion", [0, 60, ALPHANUMERISCH]],
'4217': ["(N)BSNR des Erstveranlassers / (N)BSNR of the Initial Instigator", [9, 9, NUMERISCH]],
'4241': ["Lebenslange Arztnummer (LANR) des Erstveranlassers Ersatzwert: 999999900 / Lifetime Doctor Number (LANR) of the Initial Instigator Default Value: 999999900", [9, 9, NUMERISCH]],
'4218': ["(N)BSNR des Überweisers / (N)BSNR of the Referrer", [9, 9, NUMERISCH]],
'4242': ["Lebenslange Arztnummer des Überweisers Ersatzwert: 999999900 / Lifetime Doctor Number of the Referrer Default Value: 999999900", [9, 9, NUMERISCH]],
'4219': ["Überweisung von anderen Ärzten Ersatzwert: unbekannt / Referral from Other Doctors Default Value: Unknown", [0, 60, ALPHANUMERISCH]],
'4220': ["Überweisung an Ersatzwert: kA / Referral to Default Value: Unknown", [0, 60, ALPHANUMERISCH], ['0102', 'sad2']],
'4221': ["Kurativ / Präventiv / ESS / bei belegärztlicher Behandlung / Curative / Preventive / ESS / in Inpatient Treatment", [1, 1, NUMERISCH]],
'4229': ["Ausnahmeindikation / Exception Indication", [5, 5, NUMERISCH]],
'4233': ["Stationäre Behandlung von ... bis ... / Inpatient Treatment from ... to ...", [16, 16, NUMERISCH]],
'4234': ["anerkannte Psychotherapie / Recognized Psychotherapy", [1, 1, NUMERISCH]],
'4235': ["Datum des Anerkennungsbescheides / Date of the Recognition Decree", [DATUM]],
'4239': ["Scheinuntergruppe / Voucher Subgroup", [2, 2, NUMERISCH]],
'4243': ["Weiterbehandelnder Arzt Ersatzwert: unbekannt / Continuing Doctor Default Value: Unknown", [0, 60, ALPHANUMERISCH]],
'4244': ["Bewilligte Leistung 5, / Approved Service 5,", [6, 6, ALPHANUMERISCH]],
'4245': ["Anzahl bewilligter Leistungen / Number of Approved Services", [0, 3, NUMERISCH]],
'4246': ["Anzahl abgerechneter Leistungen / Number of Billed Services", [0, 3, NUMERISCH]],
'4247': ["Antragsdatum Anerkennungsbescheid / Application Date Recognition Decree", [DATUM]],
'4261': ["Kurart / Type of Spa Treatment", [1, 1, NUMERISCH]],
'4262': ["Durchführung als Kompaktkur / Execution as Compact Cure", [1, 1, NUMERISCH]],
'4263': ["genehmigte Kurdauer in Wochen / Approved Spa Duration in Weeks", [0, 2, NUMERISCH]],
'4264': ["Anreisetag / Arrival Day", [DATUM]],
'4265': ["Abreisetag / Departure Day", [DATUM]],
'4266': ["Kurabbruch am / Spa Treatment Interruption on", [DATUM]],
'4267': ["Bewilligte Kurverlängerung in Wochen / Approved Spa Extension in Weeks", [0, 2, NUMERISCH]],
'4268': ["Bewilligungsdatum Kurverlängerung / Approval Date of Spa Extension", [DATUM]],
'4269': ["Verhaltenspräventive Maßnahmen angeregt / Behavioral Preventive Measures Encouraged", [1, 1, NUMERISCH]],
'4270': ["Verhaltenspräventive Maßnahmen durchgeführt / Behavioral Preventive Measures Carried Out", [1, 1, NUMERISCH]],
'4271': ["Kompaktkur nicht möglich / Compact Cure Not Possible", [1, 1, NUMERISCH]],
'5000': ["Leistungstag / Day of Service", [DATUM]],
'5002': ["Art der Untersuchung / Type of Examination", [0, 60, ALPHANUMERISCH]],
'5005': ["Multiplikator / Multiplier", [2, 2, NUMERISCH]],
'5006': ["Um-Uhrzeit / At Time", [4, 4, NUMERISCH]],
'5008': ["DKM", [0, 3, NUMERISCH]],
'5009': ["freier Begründungstext / Free Justification Text", [0, 60, ALPHANUMERISCH]],
'5011': ["Sachkosten-Bezeichnung / Material Cost Designation", [0, 60, ALPHANUMERISCH]],
'5012': ["Sachkosten/Materialkosten in Cent / Material Costs in Cents", [0, 10, NUMERISCH]],
'5013': ["Prozent der Leistung / Percentage of Service", [3, 3, NUMERISCH]],
'5015': ["Organ / Organ", [0, 60, ALPHANUMERISCH]],
'5016': ["Name des Arztes / Name of the Doctor", [0, 60, ALPHANUMERISCH]],
'5017': ["Besuchsort bei Hausbesuchen / Visit Location for Home Visits", [0, 60, ALPHANUMERISCH]],
'5018': ["Zone bei Besuchen / Zone for Visits", [2, 2, ALPHANUMERISCH]],
'5019': ["Erbringungsort/Standort des Gerätes / Place of Provision/Location of the Device", [0, 60, ALPHANUMERISCH]],
'5020': ["Wiederholungsuntersuchung / Repeat Examination", [1, 1, NUMERISCH]],
'5021': ["Jahr der letzten Krebsfrüherkennungsuntersuchung / Year of the Last Cancer Screening", [4, 4, NUMERISCH]],
'5023': ["GO-Nummern-Zusatz / GO Number Addition", [1, 1, ALPHANUMERISCH]],
'5024': ["GNR-Zusatzkennzeichen poststationär erbrachte Leistungen / GNR Additional Sign for Post-Hospital Services", [1, 1, ALPHANUMERISCH]],
'5025': ["Aufnahmedatum / Admission Date", [DATUM]],
'5026': ["Entlassungsdatum / Discharge Date", [DATUM]],
'5034': ["OP-Datum / Surgery Date", [DATUM]],
'5035': ["OP-Schlüssel / Surgery Key", [0, 8, ALPHANUMERISCH]],
'5036': ["GNR als Begründung 5, / GNR as Justification 5,", [6, 6, ALPHANUMERISCH]],
'5037': ["Gesamt-Schnitt-Naht-Zeit(Minuten) / Total Incision-Suture Time (Minutes)", [0, 3, NUMERISCH]],
'5038': ["Komplikation / Complication", [0, 60, ALPHANUMERISCH]],
'5040': ["Patientennummer (EDV) des FEK-Bogens / Patient Number (EDP) of the FEK Form", [0, 8, ALPHANUMERISCH]],
'5041': ["Seitenlokalisation OPS / Side Localization OPS", [1, 1, ALPHANUMERISCH]],
'5042': ["Mengenangabe KM /AM / Quantity Specification KM /AM", [0, 5, NUMERISCH]],
'5043': ["Maßeinheit KM /AM / Unit of Measure KM /AM", [1, 1, NUMERISCH]],
'5044': ["Betriebswirtschaftlich kalkulierter Preis in Cent / Economically Calculated Price in Cents", [0, 6, NUMERISCH]],
'5070': ["OMIM-G-Kode des untersuchten Gens Ersatzwert: 999999 / OMIM-G Code of the Examined Gene Default Value: 999999", [6, 6, NUMERISCH]],
'5071': ["OMIM-P-Kode (Art der Erkrankung) Ersatzwert: 999999 / OMIM-P Code (Type of Disease) Default Value: 999999", [6, 6, NUMERISCH]],
'5072': ["Gen-Name / Gene Name", [0, 60, ALPHANUMERISCH]],
'5073': ["Art der Erkrankung / Type of Disease", [0, 60, ALPHANUMERISCH]],
'5098': ["(N)BSNR des Ortes der Leistungserbringung / (N)BSNR of the Place of Service Provision", [9, 9, NUMERISCH]],
'5099': ["Lebenslange Arztnummer (LANR) des Leistungserbringers Ersatzwert: 999999900 / Lifetime Doctor Number (LANR) of the Service Provider Default Value: 999999900", [9, 9, NUMERISCH]],
'6003': ["Diagnosensicherheit / Diagnostic Certainty", [1, 1, ALPHANUMERISCH]],
'6004': ["Seitenlokalisation / Side Localization", [1, 1, ALPHANUMERISCH]],
'6006': ["Diagnosenerläuterung / Diagnosis Explanation", [0, 60, ALPHANUMERISCH]],
'6008': ["Diagnosenausnahmetatbestand / Diagnosis Exception Condition", [0, 60, ALPHANUMERISCH]],
'8000': ["Satzart / Sentence Type", [4, 4, ALPHANUMERISCH]],
'9102': ["Empfänger / Recipient", [2, 2, NUMERISCH]],
'9103': ["Erstellungsdatum / Creation Date", [DATUM]],
'9106': ["verwendeter Zeichensatz / Character Set Used", [1, 1, NUMERISCH]],
'9115': ["Erstellungsdatum ADT-Datenpaket / Creation Date ADT Data Package", [DATUM]],
'9116': ["Erstellungsdatum KADT-Datenpaket / Creation Date KADT Data Package", [DATUM]],
'9122': ["Erstellungsdatum SADT-Datenpaket / Creation Date SADT Data Package", [DATUM]],
'9132': ["enthaltene Datenpakete dieser Datei / Data Packages Contained in This File", [1, 1, ALPHANUMERISCH]],
'9204': ["Abrechnungsquartal / Billing Quarter", [5, 5, NUMERISCH]],
'9212': ["Version der Satzbeschreibung / Version of the Sentence Description", [0, 11, ALPHANUMERISCH]],
'9250': ["AVWG-Prüfnummer der AVS / AVWG Test Number of the AVS", [15, 17, ALPHANUMERISCH]],
'9260': ["Anzahl Teilabrechnungen / Number of Partial Billings", [2, 2, NUMERISCH]],
'9261': ["Abrechnungsteil x von y / Billing Part x of y", [2, 2, NUMERISCH]],
'9901': ["Systeminterner Parameter / System Internal Parameter", [0, 60, ALPHANUMERISCH]],
'3673': ["Dauerdiagnose (ICD-Code) / Chronic Diagnosis (ICD-Code)", [3, 3, 5, 6, ALPHANUMERISCH]],
'4236': ["Abklärung somatischer Ursachen vor Aufnahme einer Psychotherapie / Clarification of Somatic Causes Before Starting Psychotherapy", [1, 1, ALPHANUMERISCH]],
'5001': ["Gebührennummer (GNR) / Fee Number (GNR)", [5, 9, GOP]],
'6001': ["ICD-Code Ersatzwert: UUU / ICD Code Default Value: UUU", [3, 3, 5, 6, ALPHANUMERISCH]]
};


def check_feldkennung(feldkennung, feldkennungswert):
    """
    Checks:
        - field identifier included in the database
        - field value meets length restrictions
        - field value meets formation rules

    Checks still need final adjustments! Principle is clear though.
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
        # last element of the array is type indication (a, d, g, n)
        type = type_info[-1]
        if type == DATUM:
            #ddmmyyyy Check incomplete!
            try:
                day = int(v[0:2])
                month = int(v[2:4])
                year = int(v[4:])
                res = (day >=1 and day <= 31) and (month>=1 and month<=12) and (year > 1900)
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
        return False, "Field identifier '%s' not included in the database!" % feldkennung
    else:
        info = ALLE_FELDKENNUNGEN[feldkennung]
        err = ""
        if not check_length(info[1], feldkennungswert):
            err += "'%s' Length restriction not met!\n" % info[0]
        if  not check_value(info[1], feldkennungswert):
            err += "'%s' Value does not meet the formation rule!\n" % info[0]

    return len(err) == 0, err
