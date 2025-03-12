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

class CompSeq(Sequence):

    def pattern_matches(self, pattern):
        """
        Naive pattern matcher. Returns the indices of the beginning of each exact match of "pattern" inside "self.seq"
        """
        length_seq = len(self.seq)
        length_pattern = len(pattern)
        matches = []
        # loop through the sequence
        for n in range(length_seq):
            if n+length_pattern > length_seq:
                break
            seqchunk = self.seq[n:n+length_pattern]
            assert len(seqchunk) == len(pattern)
            if seqchunk == pattern:
                matches.append(n)
        return matches

    def hamming_distance(self, seqobj, norm=False):
        """
        Returns hamming distance between "self.seq" and "seqobj.seq". Returns None if sequences don't have the same length.
        """
        if len(self.seq) != len(seqobj.seq):
            print('Warning: Cannot calculate Hamming distance. Sequences do not have the same length')
            return None
        distance = 0
        for i in range(len(self.seq)):
            if self.seq[i] != seqobj.seq[i]:
                distance += 1
        if norm:
            distance = distance / len(self.seq)
        return distance



#####################################################################################################
def read_multifasta(path):
    col = {}
    with open(path) as fh:
        for line in fh:
            if line.startswith('>'):
                header = line.strip()
                col[header] = ''
            else:
                col[header] += line.strip()
                
    seqobjects = []
    for header, seq in col.items():
        seqobjects.append(CompSeq(header, seq))
    return seqobjects


#####################################################################################################

def main():
    seqobjects = read_multifasta(sys.argv[1])
    first_object = seqobjects[0]
    pattern = sys.argv[2]
    pattern_matches = first_object.pattern_matches(pattern)
    print(f'Matches of "{pattern}" at: {pattern_matches}')
    
    print('\nAbsolute Hamming Distances')
    for i, seqobject in enumerate(seqobjects, 1):
        hd = first_object.hamming_distance(seqobject)    
        print(f'Hamming Distance Seq1 vs Seq{i} = {hd}')

    print('\nRelative Hamming Distances')
    for i, seqobject in enumerate(seqobjects, 1):
        hd = first_object.hamming_distance(seqobject, norm=True)
        if isinstance(hd, float):
            hd = round(hd, 3)
        print(f'Hamming Distance Seq1 vs Seq{i} = {hd}')
    
# make sure script is only executed when called from the commandline (not when imported)
if __name__ == "__main__":
    main()

    
