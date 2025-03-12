__author__ = "8304676, Kartmann"


class Sequence:
    """
    Represents a biological sequence with header and sequence data.
    """

    def __init__(self, sequence, header):
        """
        Initialize a Sequence object.

        Args:
            sequence (str): The biological sequence.
            header (str): The header associated with the sequence.
        """
        self.sequence = sequence
        self.header = header
        self.genename = self.find_genename()
        self.alphabet = self.find_alphabet()
        self.frequency = self.find_frequency()


    def find_genename(self):
        """
        Extract the gene name from the header and return the entire content following "GN=".

        Returns:
            str: The entire gene name line or part following "GN=".
        """
        genename_marker = "GN="
        start = self.header.find(genename_marker)
        if start != -1:
            start += len(genename_marker)
            end = self.header.find(" ", start)
            if end == -1:
                return self.header[start:]
            return self.header[start:end]
        return ""

    def find_alphabet(self):
        """
        Determine the alphabet type (DNA or protein) based on the sequence content.

        Returns:
            str: The alphabet type ("DNA" or "Protein").
        """
        dna_chars = set("ACGTN")  # Includes 'N' for unknown bases in DNA
        protein_chars = set("ACDEFGHIKLMNPQRSTVWYBXZ")
        sequence_set = set(self.sequence.upper())

        if sequence_set.issubset(dna_chars):
            return "DNA"
        elif sequence_set.issubset(protein_chars):
            return "Protein"
        return "Unknown"

    def find_frequency(self):
        """
        Calculate the frequency of each character in the sequence.

        Returns:
            dict: A dictionary mapping characters to their frequencies.
        """
        frequency_dict = {}
        for char in self.sequence.upper():
            if char in frequency_dict:
                frequency_dict[char] += 1
            else:
                frequency_dict[char] = 1
        return frequency_dict


def read_fasta(filename):
    """
    Read a FASTA file and extract the header and sequence.

    Args:
        filename (str): Path to the FASTA file.

    Returns:
        tuple: A tuple containing the header (str) and sequence (str).
    """
    header = ""
    sequence = ""
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if header:  # If a header has already been found, break to avoid multiple sequences
                    break
                header = line[1:]
            else:
                sequence += line
    return header, sequence


def main():
    fasta_file = input("Please enter the name of the FASTA file: ")
    header, sequence = read_fasta(fasta_file)
    seq = Sequence(sequence, header)

    print(f"Genename: {seq.genename}")
    print(f"Alphabet: {seq.alphabet}")
    print(f"Frequencies: {seq.frequency}")


if __name__ == "__main__":
    main()


# Testfall:
# Please enter the name of the FASTA file: sequence.fasta
# Genename: HIV-1
# Alphabet: DNA
# Frequencies: {'A': 341, 'C': 144, 'T': 215, 'G': 188, 'N': 111}
#
# Process finished with exit code 0

