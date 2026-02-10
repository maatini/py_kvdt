py_kvdt
=======

Python-Funktionalität zum Parsen und Verarbeiten von KVDT-Dateien.

KVDT steht für Kassenärztliche Vereinigung-Datentransfer und definiert ein
Datenformat zur Übermittlung von Abrechnungsinformation vom Arzt zur
Kassenärztlichen Vereinigung. Weitere Info unter http://de.wikipedia.org/wiki/KVDT

## Funktionalitäten

Die aktuelle Version der Quellen beinhaltet folgende Funktionalitäten:

- Prüfen der Felder auf validen Feldinhalt
- Prüfen der Satzstruktur gegen Definition
- Parsen der Sätze und Auswertungen/ Transformation einige Unterstrukturen

Das Prüfen der Feldinhalte sowie der Satzarten erfolgt "tabellengesteuert". Diese
Tabellen/ Definitionen sind in den Dateien "kvdt_feld_stm.py" und "kvdt_satzarten.py"
nebst Erläuterungen enthalten.

## Installation

1. Klone das Repository: `git clone https://github.com/maatini/py_kvdt.git`
2. Navigiere in das Verzeichnis: `cd py_kvdt`
3. Stelle sicher, dass Python 3 installiert ist.
4. Führe das Demo aus: `python kvdt_main.py <datei.con>` (Beispiel-Datei im Repo enthalten)

Keine externen Abhängigkeiten erforderlich.

## Verwendung

### Demo

Führe `python kvdt_main.py <pfad_zur_kvdt_datei>` aus, um eine KVDT-Datei zu parsen und zu validieren.

Beispiel:
```
python kvdt_main.py Z05123456699_27.01.2024_12.00.con
```

### API

- `check_kvdt_felder(tokens)`: Prüft Feldinhalte gegen Definitionen.
- `parse_struktur(lexer, struktur)`: Parst eine Struktur rekursiv.
- `parse(saetze)`: Parst eine Liste von Sätzen.
- `parse_demo(file_spec)`: Demo-Funktion zum Parsen einer Datei.

### Satzarten

Unterstützte Satzarten sind in `kvdt_satzarten.py` definiert, z.B.:
- `besa`: Abrechnungsinformationen
- `con0/con9`: Container-Struktur
- ADT-Pakete: Spezifische Abrechnungsdaten

### Felddefinitionen

Feldprüfungen in `kvdt_feld_stm.py` basierend auf Regeln wie R743.

## Beispiele

Siehe `kvdt_main.py` für ein vollständiges Beispiel. Eine Beispiel-KVDT-Datei ist im Repository enthalten.

## Lizenz

GPL v3. Siehe LICENCE-Datei.

## Beitrag

Issues und Pull Requests willkommen. Für Fragen: martin.richardt@googlemail.com




