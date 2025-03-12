from Bio import AlignIO
from collections import defaultdict

# Liste der kleinen MSA-Dateien
msa_files = [
    "555_MSA.aln-clustalw",
    "582_MSA.aln-clustalw",
    "665_MSA.aln-clustalw",
    "669_MSA.aln-clustalw",
    "743_MSA.aln-clustalw",
    "1061_MSA.aln-clustalw",
    "1871_MSA.aln-clustalw"
]

# Dictionary zur Speicherung der langen Sequenzen für jedes Taxon
taxon_sequences = defaultdict(str)

# Verarbeitung jeder MSA-Datei
for msa_file in msa_files:
    print(f"Verarbeite {msa_file}...")
    # Lade das MSA im CLUSTALW-Format
    alignment = AlignIO.read(msa_file, "clustal")

    # Füge die Sequenzen für jedes Taxon hinzu
    for record in alignment:
        taxon_sequences[record.id] += str(record.seq)

# Schreibe das große MSA in eine neue FASTA-Datei
with open("concatenated_msa.fasta", "w") as output_handle:
    for taxon, sequence in taxon_sequences.items():
        output_handle.write(f">{taxon}\n")
        output_handle.write(f"{sequence}\n")

print("Konkatenation abgeschlossen: 'concatenated_msa.fasta' erstellt.")
