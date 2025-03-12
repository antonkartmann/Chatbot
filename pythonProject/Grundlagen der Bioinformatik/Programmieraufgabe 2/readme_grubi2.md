# FASTA-Sequenz-Analysator

Dieses Python-Skript liest biologische Sequenzen im FASTA-Format und extrahiert Informationen wie die Häufigkeit jedes Zeichens in der Sequenz, den Typ des Alphabets (DNA oder Protein) und den Gen-Namen aus der Kopfzeile. Zusätzlich bietet es Funktionen zur Suche nach Motiv-Übereinstimmungen und zur Berechnung der Hamming-Distanz zwischen Sequenzen.

## Funktionen

- **Kopfzeile und Sequenz extrahieren**: Liest eine FASTA-Datei und extrahiert die zugehörige Kopfzeile und Sequenz.
- **Häufigkeit berechnen**: Berechnet die Häufigkeit jedes Nukleotids oder jeder Aminosäure in der Sequenz.
- **Alphabet bestimmen**: Identifiziert, ob die Sequenz DNA, Protein oder unbekannt ist, basierend auf ihrem Inhalt.
- **Gen-Namen extrahieren**: Versucht den Gen-Namen aus der Kopfzeile der Sequenz zu extrahieren.
- **Motiv-Übereinstimmungen finden**: Gibt die Indizes aller Übereinstimmungen eines Motivs in der Sequenz zurück.
- **Hamming-Distanz berechnen**: Berechnet die Hamming-Distanz zu einer zweiten Sequenz mit der Option zur Normalisierung.

## Voraussetzungen

Dieses Skript benötigt Python 3.6 oder höher. Es werden keine externen Bibliotheken benötigt.

## Nutzung

1. **Laden Sie die FASTA-Dateien in denselben Ordner wie das Python-Programm**.
2. **Führen Sie das Programm aus**:
   ```sh
   python Programmieraufgabe2.py [motif] [filename] [--normalize]

