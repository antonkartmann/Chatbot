__author__ = '8304676, Kartmann'

from ex01 import Sequence

class CompSeq(Sequence):

    def __init__(self, header, seq, name='', normalize_frequency=False):
        super().__init__(header, seq, name, normalize_frequency)
        self.header = header
        self.seq = seq

    def pattern_matches(self, motif):
        """Return the indices of all matches of the motif in the sequence."""
        matches = []
        len_text = len(self.seq)
        len_motif = len(motif)

        for i in range(len_text - len_motif + 1):
            found = True

            for j in range(len_motif):
                if self.seq[i + j] != motif[j]:
                    found = False
                    break
            if found:
                matches.append(i)

        return matches


    def hamming_distance(self, seq1, seq2, normalize=False):
        len_seq1 = len(seq1)
        len_seq2 = len(seq2)
        if len(seq1) != len_seq2:
            raise ValueError("Sequences must be of equal length!")
        hamming_distance = 0
        for i in range(len_seq1):
            if seq1[i] != seq2[i]:
                hamming_distance += 1

        if normalize:
            norm_value = hamming_distance / len_seq1
            return hamming_distance, norm_value

        return hamming_distance


def read_multifasta(filename):
    """Read a multi-FASTA file and return a list of Sequence objects."""
    sequences = []
    with open(filename, 'r') as file:
        header = ''
        seq = ''
        for line in file:
            if line.startswith('>'):
                if header:
                    sequences.append(Sequence(header, seq))
                header = line.strip()
                seq = ''
            else:
                seq += line.strip()
        if header:
            sequences.append(Sequence(header, seq))
    return sequences


def main():
    """Main function to demonstrate pattern matching and Hamming distance calculations."""
    import argparse
    parser = argparse.ArgumentParser(description="Process some sequences.")
    parser.add_argument('motif', type=str, help='The motif to search for in the sequences')
    parser.add_argument('filename', type=str, help='The FASTA file containing the sequences')
    parser.add_argument('--normalize', action='store_true', help='Normalize the Hamming distance')
    args = parser.parse_args()

    # Read sequences from the specified FASTA file
    sequences = read_multifasta(args.filename)
    motif = args.motif
    normalize = args.normalize

    print(f"Searching for motif '{motif}' in sequences from {args.filename}")

    # Search for motif matches in each sequence
    for seq in sequences:
        comp_seq = CompSeq(seq.header, seq.seq)  # Create a CompSeq object
        matches = comp_seq.pattern_matches(motif)
        print(f"Sequence {seq.header} matches at positions: {matches}")

    # Calculate the Hamming distance between the first sequence and the other sequences
    first_seq = CompSeq(sequences[0].header, sequences[0].seq)
    for seq in sequences[1:]:
        comp_seq = CompSeq(seq.header, seq.seq)
        try:
            if normalize:
                distance, norm_value = first_seq.hamming_distance(first_seq.seq, comp_seq.seq, normalize)
                print(f"Hamming distance between {sequences[0].header} and {seq.header}: {distance} (normalized: {norm_value})")
            else:
                distance = first_seq.hamming_distance(first_seq.seq, comp_seq.seq)
                print(f"Hamming distance between {sequences[0].header} and {seq.header}: {distance}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
