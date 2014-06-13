py_kvdt
=======

Python-Funktionalität zum Parsen und Verarbeiten von KVDT-Dateien.

KVDT steht für Kassenärztliche Vereinigung-Datentransfer und definiert ein 
Datenformat zur Übermittlung von Abrechnungsinformation vom Arzt zur 
Kassenärztlichen Vereinigung. Weitere Info unter http://de.wikipedia.org/wiki/KVDT

Die aktuelle Version der Quellen beinhaltet folgende Funktionalitäten

- Prüfen der Felder auf validen Feldinhalt
- Prüfen der Satzstruktur gegen Definition
- Parsen der Sätze und Auswertungen/ Transformation einige Unterstrukturen

Das Prüfen der Feldinhalte sowie der Satzarten erfolgt "tabellengesteuert". Diese
Tabellen/ Definitionen sind in den Dateien "kvdt_feld_stm.py" und "kvdt_satzarten.py"
nebst Erläuterungen enthalten. 




