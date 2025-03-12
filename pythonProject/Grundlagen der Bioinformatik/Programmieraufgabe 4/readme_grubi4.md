# Programmieraufgabe 4: Sequenz-Aligner

Dieses Python-Skript führt Sequenzalignierungen mit den Needleman-Wunsch- und Smith-Waterman-Algorithmen durch. Es verwendet eine FASTA-Datei als Eingabe, die mindestens zwei Sequenzen enthalten muss.

## Funktionen

- **FASTA-Datei lesen**: Liest eine FASTA-Datei und extrahiert die Sequenzen.
- **Alphabet überprüfen**: Überprüft, ob die beiden Sequenzen das gleiche Alphabet verwenden.
- **Needleman-Wunsch-Algorithmus**: Führt eine globale Sequenzalignierung durch und gibt die ausgerichteten Sequenzen und die Scoring-Matrix zurück.
- **Smith-Waterman-Algorithmus**: Führt eine lokale Sequenzalignierung durch und gibt die ausgerichteten Sequenzen und die Scoring-Matrix zurück.
- **Ausrichtung drucken**: Druckt die ausgerichteten Sequenzen und die Scoring-Matrix.

## Voraussetzungen

Dieses Skript benötigt Python 3.6 oder höher. Es werden keine externen Bibliotheken benötigt.

## Nutzung

1. **Laden Sie die FASTA-Datei in denselben Ordner wie das Python-Programm**.
2. **Führen Sie das Programm aus**:
   ```sh
   python Programmieraufgabe4.py <fasta_file>


