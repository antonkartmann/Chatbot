import sys

class Sequence():

    def __init__(self, header, seq, name='', normalize_frequency=False):
        self.header = header
        self.seq = seq
        
        # assign name
        if name:
            self.genename = name
        else:
            self.genename = self.extract_genename()

        # additional information
        self.alphabet = self.identify_alphabet()
        self.frequencies = self.identify_frequencies(normalize_frequency)


    def identify_alphabet(self):
        dnachars = {
            "A", "a", "T", "t", "G", "g", "C", "c", "N"
        }
        protchars = {
            "A", "R", "N", "D", "C", "Q", "E", "G", "H", 
            "I", "L", "K", "M", "F", "P", "O", "S", "U", 
            "T", "W", "Y", "V", "B", "Z", "X", "J"
        }
        if set(self.seq).issubset(dnachars):
            return 'dna'
        elif set(self.seq).issubset(protchars):
            return 'aa'
        else:
            return 'NA'


    def extract_genename(self):
        if 'GN=' in self.header:
            return self.header.split('GN=')[1].split()[0]
        else:
            return ''


    def identify_frequencies(self, normalize_frequency):
        """
        functionality of collections.Counter 
        """
        counter = {}
        for char in self.seq:
            if not char in counter:
                counter[char] = 0
            counter[char] += 1

        if normalize_frequency:
            for char, count in counter.items():
                counter[char] = round(count / len(self.seq), 2)
        return counter


# static methods
def read_fasta(path):
    seq = ''
    with open(path) as fh:
        for line in fh:
            if line.startswith('>'):
                header = line.strip()
            else:
                seq += line.strip()
    return header, seq


# main
def main():
    scriptname = sys.argv[0]
    first_argument = sys.argv[1]
    # first_argument = 'gene.fa'

    header, seq = read_fasta(first_argument)
    s = Sequence(header, seq)
    print(f'Name: {s.genename}')
    print(f'Alphabet: {s.alphabet}')
    print('Frequencies:')
    print(s.frequencies)
    print('Normalized Frequencies:')
    print(s.identify_frequencies(normalize_frequency=True))
    

# make sure script is only executed when called from the commandline (not when imported)
if __name__ == "__main__":
    main()