# FASTA-Sequenz-Analysator

Dieses Python-Skript liest biologische Sequenzen im FASTA-Format und extrahiert Informationen wie die Häufigkeit jedes
Zeichens in der Sequenz, den Typ des Alphabets (DNA oder Protein) und den Gen-Namen aus der Kopfzeile.

## Funktionen

- Kopfzeile und Sequenz extrahieren: Liest eine FASTA-Datei und extrahiert die zugehörige Kopfzeile und Sequenz.
- Häufigkeit berechnen: Berechnet die Häufigkeit jedes Nukleotids oder Aminosäure in der Sequenz.
- Alphabet bestimmen: Identifiziert, ob die Sequenz DNA, Protein oder unbekannt ist, basierend auf ihrem Inhalt.
- Gen-Namen extrahieren: Versucht den Gen-Namen aus der Kopfzeile der Sequenz zu extrahieren.

## Voraussetzungen

Dieses Skript benötigt Python 3.6 oder höher. Es werden keine externen Bibliotheken benötigt.

## Nutzung

1. Laden Sie die Fasta Datei in den gleichen Ordner wie das Python Programm
2. Führen Sie das Programm aus
3. Geben Sie den Datei-Namen, der Fasta Datei in die Konsole ein und drücken Sie Enter

==> Mein Beispielaufruf, ruft die Fasta-Datei mit dem Namen sequence.fasta auf, die im selben Ordner gespeichert ist.

Anmerkung: Das "GN=" musste ich selber in die Kopfzeile hinzufügen, da es in der Fasta-Datei nicht vorhanden war.

