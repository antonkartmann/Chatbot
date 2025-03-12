# Phylogenetic Tree Construction Tool

Dieses Python-Programm bietet die Hauptfunktion des Berechnens eines phylogenetischen Baums mittels der UPGMA-Methode aus FASTA-Dateien.

## Anforderungen
- Python 3.x
- Die Python-Bibliotheken `math` und `argparse`

## Benutzung
Das Programm kann über die Kommandozeile mit verschiedenen Befehlen ausgeführt werden.

## Funktionen

### `read_multifasta(filepath)`
Liest Sequenzen aus einer FASTA-Datei und gibt diese als Dictionary zurück.

### `DistanceMatrix.__init__(self, filepath)`
Initialisiert die `DistanceMatrix`-Klasse und berechnet die Jukes-Cantor-korrigierte Matrix.

### `DistanceMatrix.compute_upgma_tree(self)`
Berechnet den phylogenetischen Baum mittels UPGMA.

### `DistanceMatrix.write_tree_to_newick(self, tree, output_filepath)`
Schreibt den phylogenetischen Baum im Newick-Format in eine Datei.

### `UPGMA(table, labels)`
Führt den UPGMA-Algorithmus aus, um einen phylogenetischen Baum zu erstellen.

## Aufruf:
```bash
python Programmieraufgabe5.py <input_fasta> <output_newick>
```
## Beispielaufruf:
```bash
python Programmieraufgabe5.py alignment.fasta tree.newick
