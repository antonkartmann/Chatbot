__author__ = '8304676, Kartmann'

import math
import argparse
from ex02 import read_multifasta

class DistanceMatrix:
    """
    Constructs Hamming distance matrix from a fasta file with
    aligned sequences. Rows can be accessed with matrix[m], values can be accessed with matrix[m][n]
    """

    def __init__(self, filepath):
        self.sequences = read_multifasta(filepath)
        self.matrix = self._compute_hamming_matrix()

    def _compute_hamming_matrix(self):
        num_sequences = len(self.sequences)
        matrix = []

        for i in range(num_sequences):
            row = []
            for j in range(num_sequences):
                if i == j:
                    row.append(0.0)  # The distance to itself is 0
                else:
                    hd = self.sequences[i].hamming_distance(self.sequences[j], norm=True)
                    row.append(hd)
            matrix.append(row)

        return matrix

    def print(self):
        """Prints the matrix in a readable format (rounded if necessary)."""
        for row in self.matrix:
            rounded_row = [round(value, 3) for value in row]
            print(rounded_row)

    def get_value(self, m, n):
        """Returns the value of the cell at row m and column n."""
        try:
            return self.matrix[m][n]
        except IndexError:
            print("Error: Index out of range. Please provide valid indices.")
            return None

    def change_value(self, m, n, new_value):
        """Sets the value of the cell at row m and column n to new_value."""
        try:
            self.matrix[m][n] = new_value
        except IndexError:
            print("Error: Index out of range. Please provide valid indices.")

    def max_value(self):
        """Returns the maximum value in the matrix."""
        max_value = -math.inf
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i != j:  # Exclude diagonal values
                    if self.matrix[i][j] > max_value:
                        max_value = self.matrix[i][j]
        return max_value

    def min_value(self):
        """Returns the minimum value in the matrix excluding diagonal values."""
        min_value = math.inf
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i != j:  # Exclude diagonal values
                    if self.matrix[i][j] < min_value:
                        min_value = self.matrix[i][j]
        return min_value

    def correct_JC(self):
        """Corrects the distances in the matrix according to the Jukes-Cantor model."""
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if i != j:
                    p = self.matrix[i][j]
                    if p < 3 / 4:
                        self.matrix[i][j] = -3 / 4 * math.log(1 - 4 / 3 * p)
                    else:
                        self.matrix[i][j] = float('inf')  # Infinite distance for p >= 3/4

def concatenate_alignment_fragments(filepaths, output_path):
    """
    Concatenates multiple alignment fragments from FASTA files, ensuring that taxa not present in
    some alignments are filled with gap characters.

    Parameters:
    filepaths (list): List of file paths to the alignment FASTA files.
    output_path (str): Path to the output FASTA file.
    """
    all_sequences = {}
    total_length = 0

    # Read all FASTA files and store sequences in a dictionary
    for filepath in filepaths:
        sequences = read_multifasta(filepath)
        alignment_length = len(sequences[0].seq) if sequences else 0
        total_length += alignment_length

        for seq_obj in sequences:
            if seq_obj.header not in all_sequences:
                all_sequences[seq_obj.header] = ['-' * total_length]  # Initialize with gaps
            all_sequences[seq_obj.header].append(seq_obj.seq)

        # Update the length of existing sequences to accommodate the new alignment
        for header in all_sequences:
            if header not in [seq_obj.header for seq_obj in sequences]:
                all_sequences[header].append('-' * alignment_length)

    # Concatenate sequences
    concatenated_sequences = {header: ''.join(parts) for header, parts in all_sequences.items()}

    # Write the concatenated sequences to the output file
    with open(output_path, 'w') as outfile:
        for header, sequence in concatenated_sequences.items():
            outfile.write(f"{header}\n")
            outfile.write(f"{sequence}\n")

def main():
    parser = argparse.ArgumentParser(description="Distance Matrix and FASTA alignment concatenation tool.")
    subparsers = parser.add_subparsers(dest='command')

    # Subparser für die DistanceMatrix Funktionalität
    parser_distance = subparsers.add_parser('distance', help='Work with Hamming distance matrices.')
    parser_distance.add_argument('filepath', type=str, nargs='?', default='align1.fasta', help='Path to the input FASTA file')

    # Subparser für die concatenate Funktionalität
    parser_concat = subparsers.add_parser('concatenate', help='Concatenate multiple alignment fragments.')
    parser_concat.add_argument('output', type=str, nargs='?', default='output.fasta', help='Path to the output FASTA file')
    parser_concat.add_argument('filepaths', metavar='F', type=str, nargs='*', default=['align1.fasta', 'align2.fasta', 'align3.fasta', 'align4.fasta'], help='Paths to the alignment FASTA files')

    args = parser.parse_args()

    if args.command is None:
        # Fallback to default behavior if no command is provided
        print("No command provided. Defaulting to distance calculation.")
        args.command = 'distance'

    if args.command == 'distance':
        print(f"Reading FASTA file from: {args.filepath}")
        distance_matrix = DistanceMatrix(args.filepath)
        print("Original Hamming Distance Matrix:")
        distance_matrix.print()

        distance_matrix.correct_JC()
        print("\nJukes-Cantor Corrected Distance Matrix:")
        distance_matrix.print()

        print("Value at (0, 1):", distance_matrix.get_value(0, 1))

        distance_matrix.change_value(0, 1, 0.5)
        print("New value at (0, 1):", distance_matrix.get_value(0, 1))

        print("Max value in matrix:", distance_matrix.max_value())
        print("Min value in matrix:", distance_matrix.min_value())

    elif args.command == 'concatenate':
        concatenate_alignment_fragments(args.filepaths, args.output)
        print(f"Concatenated alignment written to {args.output}")

if __name__ == "__main__":
    main()
