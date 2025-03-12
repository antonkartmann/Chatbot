# Distance Matrix and FASTA Alignment Concatenation Tool

Dieses Python-Programm bietet zwei Hauptfunktionen: das Berechnen von Hamming-Distanzmatrizen aus FASTA-Dateien und das Zusammenführen von FASTA-Ausrichtungsfragmenten.

## Anforderungen

- Python 3.x
- Die Python-Bibliotheken `math` und `argparse`
- Ein Modul `ex02` mit einer Funktion `read_multifasta`, die eine FASTA-Datei liest und die Sequenzen zurückgibt.


## Benutzung

Das Programm kann über die Kommandozeile mit verschiedenen Befehlen ausgeführt werden.

### Befehle

1. **distance**: Berechnet die Hamming-Distanzmatrix für eine gegebene FASTA-Datei.

    **Syntax**:
    ```bash
    python Programmieraufgabe_3.py distance <filepath>
    ```
    **Beispiel**:
    ```bash
    python Programmieraufgabe_3.py distance align1.fasta
    ```

    **Parameter**:
    - `<filepath>`: Der Pfad zur Eingabe-FASTA-Datei.

2. **concatenate**: Führt mehrere FASTA-Ausrichtungsfragmente zusammen.

    **Syntax**:
    ```bash
    python Programmieraufgabe_3.py concatenate <output> <filepaths...>
    ```
    **Beispiel**:
    ```bash
    python Programmieraufgabe_3.py concatenate output.fasta align1.fasta align2.fasta align3.fasta align4.fasta
    ```

    **Parameter**:
    - `<output>`: Der Pfad zur Ausgabe-FASTA-Datei.
    - `<filepaths...>`: Eine Liste von Pfaden zu den Eingabe-FASTA-Dateien.

### Standardverhalten

Wenn kein Befehl angegeben wird, wird das Programm standardmäßig den `distance`-Befehl mit der Datei `align1.fasta` ausführen.

**Syntax ohne Parameter**:
```bash
python Programmieraufgabe_3.py
