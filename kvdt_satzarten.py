
s0101 = [
    ["8000", "Satzart", 1, "m",  [], []],
    ["3000", "Patientennummer", 1, "k",  [], []],
    ["3003", "Schein_ID", 1, "k",  [], []],
    ["3004", "KartentypRegel", 1, "m",  ["R306"], []],
    ["3006", "Version", 1, "m",  ["R397"], []],
    ["3100", "Namenszusatz", 1, "k",  [], []],
    ["3101", "Name", 1, "m",  [], []],
    ["3102", "Vorname", 1, "m",  [], []],
    ["3103", "Geburtsdatum", 1, "m",  [], []],
    ["3104", "Titel", 1, "k",  [], []],
    ["3105", "Versichertennummer", 1, "m",  ["R752"], []],
    ["3119", "Versichertennummer_eGK", 1, "m",  ["R752"], []],
    ["3107", "Straße", 1, "k",  [], []],
    ["3112", "PLZ", 1, "m",  ["R479"], []],
    ["3114", "Wohnsitzländercode", 1, "k",  [], []],
    ["3113", "Wohnort", 1, "k",  [], []],
    ["3116", "KV_Bereich", 1, "k",  [], []],
    ["3108", "Versichertenart", 1, "m",  [], []],
    ["3110", "Geschlecht", 1, "m",  [], []],
    ["4101", "Quartal", 1, "m",  [], []],
    ["4102", "Ausstellungsdatum", 1, "k",  [], []],
    ["4104", "Abrechnungs_VKNR", 1, "m",  [], []],
    ["4106", "Kostenträger", 1, "m",  [], []],
    ["4108", "Zulassungsnummer", 1, "k",  [], []],
    ["4109", "Letzter_Einlesetag", 1, "m",  [], []],
    ["4110", "Gültigkeit_Bis", 1, "m",  ["R752"], []],
    ["4111", "Krankenkassennummer", 1, "m",  [], []],
    ["4112", "Versichertenstatus", 1, "m",  ["R752"], []],
    ["4113", "Statusergänzung", 1, "m",  ["R752"], []],
    ["4121", "Gebührenordnung", 1, "m",  [], []],
    ["4122", "Abrechnungsgebiet", 1, "m",  [], []],
    ["4123", "Personenkreis", 1, "k",  [], []],
    ["4124", "SKT_Zusatzangaben", 1, "k",  [], []],
    ["4125", "Gültigkeitszeitraum", 1, "k",  [], []],
    ["4126", "SKT_Bemerkungen", 0, "k",  [], []],
    ["4202", "Unfall", 1, "k",  [], []],
    ["4204", "Leistungsanspruch", 1, "k",  [], []],
    ["4206", "Tag_der_Entbindung", 1, "k",  [], []],
    ["4234", "anerkannte_Psychotherapie", 1, "k",  [], [
        ["4235", "Datum_des_Anerkennungsbescheides", 0, "m",  [], [
            ["4247", "Antragsdatum", 1, "k",  [], []],
            ["4244", "Bewilligte_Leistung", 0, "k",  [], [
                ["4245", "Anzahl_bewilligter_Leistungen", 1, "m",  [], []], 
                ["4246", "Anzahl_abgerechneter_Leistungen", 1, "m",  [], []]]
            ]          
        ]]]
    ],    
    ["4236", "Abklärung_somatischer_Ursachen", 1, "k",  [], []],
    ["4239", "Scheinuntergruppe", 1, "m",  [], []],
    

    ["5000", "Leistungstag", 0, "m",  [], [
        ["5001", "GNR", 0, "m",  [], [
            ["5002", "Art_der_Untersuchung", 1, "k",  [], []],
            ["5005", "Multiplikator", 1, "k",  [], []],
            ["5006", "Um_Uhrzeit", 1, "k",  [], []],
            ["5008", "DKM", 1, "k",  [], []],
            ["5009", "Begründungstext", 0, "k",  [], []],
            ["5012", "Sachkosten", 0, "k",  [], [
                ["5011", "Sachkosten_Bezeichnung", 0, "m",  [], []]]
            ],

            ["5013", "Prozent_der_Leistung", 1, "k",  [], []],
            ["5015", "Organ", 0, "k",  [], []],
            ["5016", "Name_des_Arztes", 0, "k",  [], []],
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
            ["5035", "OP-Schlüssel", 0, "k",  [], [
                ["5041", "Seitenlokalisation_OPS", 1, "k",  [], []]]
            ],
            ["5036", "GNR_als_Begründung", 0, "k",  [], []],
            ["5037", "Simultaneingriff", 1, "m",  [], []],
            ["5038", "Komplikation", 0, "k",  [], []],
            ["5040", "Patientennummer", 1, "k",  [], []],
            ["5042", "Mengenangabe", 1, "k",  [], [
                ["5043", "Maßeinheit", 1, "m",  [], []]]
            ],
            ["5070", "OMIM_G_KODE", 1, "m",  ["R770"], []],
            ["5071", "OMIM_P_KODE", 1, "m",  ["R770"], [
                ["5072", "Gen_Name", 0, "m",  ["R772"], []], 
                ["5073", "Art_der_Erkrankung", 0, "m",  ["R773"], []]]
            ],
            ["5098", "BSNR", 1, "m",  [], []],
            ["5099", "LANR", 1, "m",  [], []]
    ]]]],    
    
    ["6001", "ICD_Code", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["6003", "Diagnosensicherheit", 1, "m",  ["R484"], []],
        ["6004", "Seitenlokalisation", 1, "k",  [], []],
        ["6006", "Diagnosenerläuterung", 0, "k",  [], []],
        ["6008", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]],
       
    ["3673", "Dauerdiagnose", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["3674", "Diagnosensicherheit", 1, "m",  [], []],
        ["3675", "Seitenlokalisation", 1, "k",  [], []],
        ["3676", "Diagnosenerläuterung", 0, "k",  [], []],
        ["3677", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]]
]    


s0102 = [
    ["8000", "Satzart", 1, "m",  [], []],
    ["3000", "Patientennummer", 1, "k",  [], []],
    ["3003", "Schein_ID", 1, "k",  [], []],
    ["3004", "KartentypRegel", 1, "m",  ["R306"], []],
    ["3006", "Version", 1, "m",  ["R397"], []],
    ["3100", "Namenszusatz", 1, "k",  [], []],
    ["3101", "Name", 1, "m",  [], []],
    ["3102", "Vorname", 1, "m",  [], []],
    ["3103", "Geburtsdatum", 1, "m",  [], []],
    ["3104", "Titel", 1, "k",  [], []],
    ["3105", "Versichertennummer", 1, "m",  ["R752"], []],
    ["3119", "Versichertennummer_eGK", 1, "m",  ["R752"], []],
    ["3107", "Straße", 1, "k",  [], []],
    ["3112", "PLZ", 1, "m",  ["R479"], []],
    ["3114", "Wohnsitzländercode", 1, "k",  [], []],
    ["3113", "Wohnort", 1, "k",  [], []],
    ["3116", "KV_Bereich", 1, "k",  [], []],
    ["3108", "Versichertenart", 1, "m",  [], []],
    ["3110", "Geschlecht", 1, "m",  [], []],
    ["4101", "Quartal", 1, "m",  [], []],
    ["4102", "Ausstellungsdatum", 1, "k",  [], []],
    ["4104", "Abrechnungs_VKNR", 1, "m",  [], []],
    ["4106", "Kostenträger", 1, "m",  [], []],
    ["4108", "Zulassungsnummer", 1, "k",  [], []],
    ["4109", "Letzter_Einlesetag", 1, "m",  [], []],
    ["4110", "Gültigkeit_Bis", 1, "m",  ["R752"], []],
    ["4111", "Krankenkassennummer", 1, "m",  [], []],
    ["4112", "Versichertenstatus", 1, "m",  ["R752"], []],
    ["4113", "Statusergänzung", 1, "m",  ["R752"], []],
    ["4121", "Gebührenordnung", 1, "m",  [], []],
    ["4122", "Abrechnungsgebiet", 1, "m",  [], []],
    ["4123", "Personenkreis", 1, "k",  [], []],
    ["4124", "SKT_Zusatzangaben", 1, "k",  [], []],
    ["4125", "Gültigkeitszeitraum", 1, "k",  [], []],
    ["4126", "SKT_Bemerkungen", 0, "k",  [], []],
    ["4202", "Unfall", 1, "k",  [], []],
    ["4204", "Leistungsanspruch", 1, "k",  [], []],
    ["4205", "Auftrag", 0, "m",  [R744, R755], []],      
    ["4206", "Tag_der_Entbindung", 1, "k",  [], []],
    
    ["4207", "Diagnose", 0, "k",  [], []],
    ["4208", "Befund", 0, "k",  [], []],
    ["4217", "BSNR_Erstveranlassers", 1, "k",  ["R431"], [
        ["4241", "LANR", 1, "m",  [], []]
    ]],
    
    ["4218", "BSNR", 1, "m",  ["R328"], [
        ["4242", "Lebenslange_Arztnummer_Überweisers", 1, "m",  [], []]
    ]],   
    ["4219", "Überweisung", 1, "m",  ["R328"], []],
    ["4220", "Überweisung", 1, "m",  ["R320"], []],
    ["4221", "Behandlung", 1, "m",  ["R404"], []],
    ["4229", "Ausnahmeindikation", 1, "k",  ["R432"], []],
    
   
    ["4234", "anerkannte_Psychotherapie", 1, "k",  [], [
        ["4235", "Datum_des_Anerkennungsbescheides", 0, "m",  [], [
            ["4247", "Antragsdatum", 1, "k",  [], []],
            ["4244", "Bewilligte_Leistung", 0, "k",  [], [
                ["4245", "Anzahl_bewilligter_Leistungen", 1, "m",  [], []], 
                ["4246", "Anzahl_abgerechneter_Leistungen", 1, "m",  [], []]]
            ]          
        ]]]
    ],    
    ["4239", "Scheinuntergruppe", 1, "m",  [], []],
    

    ["5000", "Leistungstag", 0, "m",  [], [
        ["5001", "GNR", 0, "m",  [], [
            ["5002", "Art_der_Untersuchung", 1, "k",  [], []],
            ["5005", "Multiplikator", 1, "k",  [], []],
            ["5006", "Um_Uhrzeit", 1, "k",  [], []],
            ["5008", "DKM", 1, "k",  [], []],
            ["5009", "Begründungstext", 0, "k",  [], []],
            ["5012", "Sachkosten", 0, "k",  [], [
                ["5011", "Sachkosten_Bezeichnung", 0, "m",  [], []]]
            ],

            ["5013", "Prozent_der_Leistung", 1, "k",  [], []],
            ["5015", "Organ", 0, "k",  [], []],
            ["5016", "Name_des_Arztes", 0, "k",  [], []],
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
            ["5035", "OP-Schlüssel", 0, "k",  [], [
                ["5041", "Seitenlokalisation_OPS", 1, "k",  [], []]]
            ],
            ["5036", "GNR_als_Begründung", 0, "k",  [], []],
            ["5037", "Simultaneingriff", 1, "m",  [], []],
            ["5038", "Komplikation", 0, "k",  [], []],
            ["5040", "Patientennummer", 1, "k",  [], []],
            ["5042", "Mengenangabe", 1, "k",  [], [
                ["5043", "Maßeinheit", 1, "m",  [], []]]
            ],
            ["5044", "Preis_in_Cent", 1, "k",  [], []],
            ["5070", "OMIM_G_KODE", 1, "m",  ["R770"], []],
            ["5071", "OMIM_P_KODE", 1, "m",  ["R770"], [
                ["5072", "Gen_Name", 0, "m",  ["R772"], []], 
                ["5073", "Art_der_Erkrankung", 0, "m",  ["R773"], []]]
            ],
            ["5098", "BSNR", 1, "m",  [], []],
            ["5099", "LANR", 1, "m",  [], []]
    ]]]],    
    
    ["6001", "ICD_Code", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["6003", "Diagnosensicherheit", 1, "m",  ["R484"], []],
        ["6004", "Seitenlokalisation", 1, "k",  [], []],
        ["6006", "Diagnosenerläuterung", 0, "k",  [], []],
        ["6008", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]],
       
    ["3673", "Dauerdiagnose", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["3674", "Diagnosensicherheit", 1, "m",  [], []],
        ["3675", "Seitenlokalisation", 1, "k",  [], []],
        ["3676", "Diagnosenerläuterung", 0, "k",  [], []],
        ["3677", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]]
]    

s0103 = [
    ["8000", "Satzart", 1, "m",  [], []],
    ["3000", "Patientennummer", 1, "k",  [], []],
    ["3003", "Schein_ID", 1, "k",  [], []],
    ["3004", "Kartentyp", 1, "m",  ["R306"], []],
    ["3006", "Version", 1, "m",  ["R397"], []],
    ["3100", "Namenszusatz", 1, "k",  [], []],
    ["3101", "Name", 1, "m",  [], []],
    ["3102", "Vorname", 1, "m",  [], []],
    ["3103", "Geburtsdatum", 1, "m",  [], []],
    ["3104", "Titel", 1, "k",  [], []],
    ["3105", "Versichertennummer", 1, "m",  ["R752"], []],
    ["3119", "Versichertennummer_eGK", 1, "m",  ["R752"], []],
    ["3107", "Straße", 1, "k",  [], []],
    ["3112", "PLZ", 1, "m",  ["R479"], []],
    ["3114", "Wohnsitzländercode", 1, "k",  [], []],
    ["3113", "Wohnort", 1, "k",  [], []],
    ["3116", "KV_Bereich", 1, "k",  [], []],
    ["3108", "Versichertenart", 1, "m",  [], []],
    ["3110", "Geschlecht", 1, "m",  [], []],
    ["4101", "Quartal", 1, "m",  [], []],
    ["4102", "Ausstellungsdatum", 1, "k",  [], []],
    ["4104", "Abrechnungs_VKNR", 1, "m",  [], []],
    ["4106", "Kostenträger", 1, "m",  [], []],
    ["4108", "Zulassungsnummer", 1, "k",  [], []],
    ["4109", "Letzter_Einlesetag", 1, "m",  [], []],
    ["4110", "Gültigkeit_Bis", 1, "m",  ["R752"], []],
    ["4111", "Krankenkassennummer", 1, "m",  [], []],
    ["4112", "Versichertenstatus", 1, "m",  ["R752"], []],
    ["4113", "Statusergänzung", 1, "m",  ["R752"], []],
    ["4121", "Gebührenordnung", 1, "m",  [], []],
    ["4122", "Abrechnungsgebiet", 1, "m",  [], []],
    ["4123", "Personenkreis", 1, "k",  [], []],
    ["4124", "SKT_Zusatzangaben", 1, "k",  [], []],
    ["4126", "SKT_Bemerkungen", 0, "k",  [], []],
    ["4202", "Unfall", 1, "k",  [], []],
    ["4204", "Leistungsanspruch", 1, "k",  [], []],
    ["4205", "Auftrag", 0, "m",  ["R746"], []],
    ["4206", "Tag_der_Entbindung", 1, "k",  [], []],    
    ["4207", "Diagnose", 0, "m",  ["R746"], []],
    ["4208", "Befund", 0, "m",  ["R746"], []],
    ["4218", "BSNR_Überweisers", 1, "m",  ["R746"], [
        ["4242", "LANR_Überweiser", 1, "m",  [], []]
    ]],    
    ["4233", "Behandlungszeitraum", 0, "m",  ["R354"], []],
    ["4239", "Scheinuntergruppe", 1, "m",  [], []],    

    ["5000", "Leistungstag", 0, "m",  [], [
        ["5001", "GNR", 0, "m",  [], [
            ["5002", "Art_der_Untersuchung", 1, "k",  [], []],
            ["5005", "Multiplikator", 1, "k",  [], []],
            ["5006", "Um_Uhrzeit", 1, "k",  [], []],
            ["5008", "DKM", 1, "k",  [], []],
            ["5009", "Begründungstext", 0, "k",  [], []],
            ["5012", "Sachkosten", 0, "k",  [], [
                ["5011", "Sachkosten_Bezeichnung", 0, "m",  [], []]]
            ],

            ["5013", "Prozent_der_Leistung", 1, "k",  [], []],
            ["5015", "Organ", 0, "k",  [], []],
            ["5016", "Name_des_Arztes", 0, "k",  [], []],
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
            ["5035", "OP-Schlüssel", 0, "k",  [], [
                ["5041", "Seitenlokalisation_OPS", 1, "k",  [], []]]
            ],
            ["5036", "GNR_als_Begründung", 0, "k",  [], []],
            ["5037", "Simultaneingriff", 1, "m",  [], []],
            ["5038", "Komplikation", 0, "k",  [], []],
            ["5040", "Patientennummer", 1, "k",  [], []],
            ["5042", "Mengenangabe", 1, "k",  [], [
                ["5043", "Maßeinheit", 1, "m",  [], []]]
            ],
            ["5070", "OMIM_G_KODE", 1, "m",  ["R770"], []],
            ["5071", "OMIM_P_KODE", 1, "m",  ["R770"], [
                ["5072", "Gen_Name", 0, "m",  ["R772"], []], 
                ["5073", "Art_der_Erkrankung", 0, "m",  ["R773"], []]]
            ],
            ["5098", "BSNR", 1, "m",  [], []],
            ["5099", "LANR", 1, "m",  [], []]
    ]]]],    
    
    ["6001", "ICD_Code", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["6003", "Diagnosensicherheit", 1, "m",  ["R484"], []],
        ["6004", "Seitenlokalisation", 1, "k",  [], []],
        ["6006", "Diagnosenerläuterung", 0, "k",  [], []],
        ["6008", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]],
       
    ["3673", "Dauerdiagnose", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["3674", "Diagnosensicherheit", 1, "m",  [], []],
        ["3675", "Seitenlokalisation", 1, "k",  [], []],
        ["3676", "Diagnosenerläuterung", 0, "k",  [], []],
        ["3677", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]]
]    

s0104 = [
    ["8000", "Satzart", 1, "m",  [], []],
    ["3000", "Patientennummer", 1, "k",  [], []],
    ["3003", "Schein_ID", 1, "k",  [], []],
    ["3004", "KartentypRegel", 1, "m",  ["R306"], []],
    ["3006", "Version", 1, "m",  ["R397"], []],
    ["3100", "Namenszusatz", 1, "k",  [], []],
    ["3101", "Name", 1, "m",  [], []],
    ["3102", "Vorname", 1, "m",  [], []],
    ["3103", "Geburtsdatum", 1, "m",  [], []],
    ["3104", "Titel", 1, "k",  [], []],
    ["3105", "Versichertennummer", 1, "m",  ["R752"], []],
    ["3119", "Versichertennummer_eGK", 1, "m",  ["R752"], []],
    ["3107", "Straße", 1, "k",  [], []],
    ["3112", "PLZ", 1, "m",  ["R479"], []],
    ["3114", "Wohnsitzländercode", 1, "k",  [], []],
    ["3113", "Wohnort", 1, "k",  [], []],
    ["3116", "KV_Bereich", 1, "k",  [], []],
    ["3108", "Versichertenart", 1, "m",  [], []],
    ["3110", "Geschlecht", 1, "m",  [], []],
    ["4101", "Quartal", 1, "m",  [], []],
    ["4104", "Abrechnungs_VKNR", 1, "m",  [], []],
    ["4106", "Kostenträger", 1, "m",  [], []],
    ["4108", "Zulassungsnummer", 1, "k",  [], []],
    ["4109", "Letzter_Einlesetag", 1, "m",  [], []],
    ["4110", "Gültigkeit_Bis", 1, "m",  ["R752"], []],
    ["4111", "Krankenkassennummer", 1, "m",  [], []],
    ["4112", "Versichertenstatus", 1, "m",  ["R752"], []],
    ["4113", "Statusergänzung", 1, "m",  ["R752"], []],
    ["4121", "Gebührenordnung", 1, "m",  [], []],
    ["4122", "Abrechnungsgebiet", 1, "m",  [], []],
    ["4123", "Personenkreis", 1, "k",  [], []],
    ["4124", "SKT_Zusatzangaben", 1, "k",  [], []],
    ["4125", "Gültigkeitszeitraum", 1, "k",  [], []],
    ["4126", "SKT_Bemerkungen", 0, "k",  [], []],
    ["4202", "Unfall", 1, "k",  [], []],
    ["4239", "Scheinuntergruppe", 1, "m",  [], []],
    ["4243", "Weiterbehandelnder_Arzt", 1, "m",  [], []],    

    ["5000", "Leistungstag", 0, "m",  [], [
        ["5001", "GNR", 0, "m",  [], [
            ["5002", "Art_der_Untersuchung", 1, "k",  [], []],
            ["5005", "Multiplikator", 1, "k",  [], []],
            ["5006", "Um_Uhrzeit", 1, "k",  [], []],
            ["5008", "DKM", 1, "k",  [], []],
            ["5009", "Begründungstext", 0, "k",  [], []],
            ["5012", "Sachkosten", 0, "k",  [], [
                ["5011", "Sachkosten_Bezeichnung", 0, "m",  [], []]]
            ],

            ["5013", "Prozent_der_Leistung", 1, "k",  [], []],
            ["5015", "Organ", 0, "k",  [], []],
            ["5016", "Name_des_Arztes", 0, "k",  [], []],
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
            ["5035", "OP-Schlüssel", 0, "k",  [], [
                ["5041", "Seitenlokalisation_OPS", 1, "k",  [], []]]
            ],
            ["5036", "GNR_als_Begründung", 0, "k",  [], []],
            ["5037", "Simultaneingriff", 1, "m",  [], []],
            ["5038", "Komplikation", 0, "k",  [], []],
            ["5040", "Patientennummer", 1, "k",  [], []],
            ["5042", "Mengenangabe", 1, "k",  [], [
                ["5043", "Maßeinheit", 1, "m",  [], []]]
            ],
            ["5070", "OMIM_G_KODE", 1, "m",  ["R770"], []],
            ["5071", "OMIM_P_KODE", 1, "m",  ["R770"], [
                ["5072", "Gen_Name", 0, "m",  ["R772"], []], 
                ["5073", "Art_der_Erkrankung", 0, "m",  ["R773"], []]]
            ],
            ["5098", "BSNR", 1, "m",  [], []],
            ["5099", "LANR", 1, "m",  [], []]
    ]]]],    
    
    ["6001", "ICD_Code", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["6003", "Diagnosensicherheit", 1, "m",  ["R484"], []],
        ["6004", "Seitenlokalisation", 1, "k",  [], []],
        ["6006", "Diagnosenerläuterung", 0, "k",  [], []],
        ["6008", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]],
       
    ["3673", "Dauerdiagnose", 0, "m",  ["R486", "R488", "R489", "R761", "R490", "R491", "R492", "R728", "R729"], [
        ["3674", "Diagnosensicherheit", 1, "m",  [], []],
        ["3675", "Seitenlokalisation", 1, "k",  [], []],
        ["3676", "Diagnosenerläuterung", 0, "k",  [], []],
        ["3677", "Diagnosenausnahmetatbestand", 0, "m",  ["R491"], []]
    ]]
]    


adt9 = ["8000", "Satzart", 1, "m",  [], []]

besa = [
    ["8000", "Satzart", 1, "m",  [], []],
    ["0201", "BSNR", 0, "m",  [], []],
    ["0203", "Bezeichnung", 1, "m",  [], []],
    ["0212", "LANR", 0, "m",  [], [
        ["0219", "Titel", 1, "k",  [], []], 
        ["0220", "Arztvorname", 1, "k",  [], []], 
        ["0221", "Namenszusatz", 1, "k",  [], []], 
        ["0211", "Arztname", 1, "m",  ["R719"], []]]
    ],
    ["0205", "Straße", 1, "m",  [], []],
    ["0215", "PLZ", 1, "m",  [], []],
    ["0216", "Ort", 1, "m",  [], []],
    ["0208", "Telefonnummer", 1, "m",  [], []],
    ["0209", "Telefaxnummer", 1, "k",  [], []],
    ["0218", "EMail", 1, "k",  [], []]
]

con0 = [
    ["8000", "Satzart", 1, "m",  [], []],
    ["9103", "Erstellungsdatum", 1, "m",  [], []],
    ["9106", "Zeichensatz", 1, "m",  [], [
        ["9132", "Datenpakete", 0, "m",  [], []]]
    ]
]

con9 = ["8000", "Satzart", 1, "m",  [], []]

rvsa = [    
    ["8000", "Satzart", 1, "m",  ["R743"], []], 
    ["0201", "BSNR", 0, "m",  [], 
        [["0300", "Laborleistungen", 1, "m",  [], 
            [["0301", "Analysen", 1, "m",  ["R740"], [
                    ["0302", "Gerätetyp", 0, "m",  ["R741"], [
                        ["0303", "Hersteller", 1, "m",  [], []]]]]], 
            ["0304", "Analyt_ID", 0, "m",  ["R740"], [
                    ["0305", "RV_Zertifikat", 1, "m",  [], []]]]]]
        ]
    ]
]




