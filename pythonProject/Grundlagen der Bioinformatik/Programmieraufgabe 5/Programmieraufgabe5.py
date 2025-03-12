__author__ = '8304676, Kartmann'

import math
import argparse

# Function to read sequences from a FASTA file
def read_multifasta(filepath):
    with open(filepath, 'r') as file:
        sequences = {}
        sequence_id = None
        sequence_data = []

        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if sequence_id is not None:
                    sequences[sequence_id] = ''.join(sequence_data)
                sequence_id = line[1:]
                sequence_data = []
            else:
                sequence_data.append(line)

        if sequence_id is not None:
            sequences[sequence_id] = ''.join(sequence_data)

    return sequences

# Class to compute the distance matrix
class DistanceMatrix:
    def __init__(self, filepath):
        sequences = read_multifasta(filepath)
        self.sequences = list(sequences.values())
        self.labels = list(sequences.keys())
        self.matrix = self._compute_jc_corrected_matrix()

    def _compute_hamming_matrix(self):
        num_sequences = len(self.sequences)
        matrix = []

        for i in range(num_sequences):
            row = []
            for j in range(num_sequences):
                if i == j:
                    row.append(0.0)
                else:
                    hd = self._hamming_distance(self.sequences[i], self.sequences[j])
                    row.append(hd)
            matrix.append(row)

        return matrix

    def _hamming_distance(self, seq1, seq2):
        assert len(seq1) == len(seq2), "Sequences must be of the same length"
        return sum(c1 != c2 for c1, c2 in zip(seq1, seq2)) / len(seq1)

    def _compute_jc_corrected_matrix(self):
        hamming_matrix = self._compute_hamming_matrix()
        num_sequences = len(hamming_matrix)
        jc_matrix = []

        for i in range(num_sequences):
            row = []
            for j in range(num_sequences):
                if i == j:
                    row.append(0.0)
                else:
                    p = hamming_matrix[i][j]
                    if p >= 0.75:
                        jc_distance = float('inf')  # Jukes-Cantor model is not defined for p >= 0.75
                    else:
                        jc_distance = -0.75 * math.log(1 - (4.0 / 3.0) * p)
                    row.append(jc_distance)
            jc_matrix.append(row)

        return jc_matrix

    def compute_upgma_tree(self):
        return UPGMA(self.matrix, self.labels)

    def write_tree_to_newick(self, tree, output_filepath):
        with open(output_filepath, 'w') as file:
            file.write(tree + ';')

# lowest_cell:
#   Locates the smallest cell in the table
def lowest_cell(table):
    min_cell = float("inf")
    x, y = -1, -1

    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j] < min_cell and i != j:
                min_cell = table[i][j]
                x, y = i, j

    return x, y

# join_labels:
#   Combines two labels in a list of labels
def join_labels(labels, a, b):
    if b < a:
        a, b = b, a

    labels[a] = "(" + labels[a] + "," + labels[b] + ")"
    del labels[b]

# join_table:
#   Joins the entries of a table on the cell (a, b) by averaging their data entries
def join_table(table, a, b):
    if b < a:
        a, b = b, a

    row = [(table[a][i] + table[b][i]) / 2 for i in range(0, a)]
    table[a] = row

    for i in range(a + 1, b):
        table[i][a] = (table[i][a] + table[b][i]) / 2

    for i in range(b + 1, len(table)):
        table[i][a] = (table[i][a] + table[i][b]) / 2
        del table[i][b]

    del table[b]

# UPGMA:
#   Runs the UPGMA algorithm on a labelled table
def UPGMA(table, labels):
    while len(labels) > 1:
        x, y = lowest_cell(table)
        join_table(table, x, y)
        join_labels(labels, x, y)

    return labels[0]

# Main function to run the script with argparse
def main():
    parser = argparse.ArgumentParser(
        description="Compute a phylogenetic tree using UPGMA from a FASTA file and save it in Newick format.")
    parser.add_argument("input_fasta", help="Path to the input FASTA file.")
    parser.add_argument("output_newick", help="Path to the output Newick file.")
    args = parser.parse_args()

    dm = DistanceMatrix(args.input_fasta)
    tree = dm.compute_upgma_tree()
    print(f"Newick format tree: {tree}")
    dm.write_tree_to_newick(tree, args.output_newick)

if __name__ == "__main__":
    main()