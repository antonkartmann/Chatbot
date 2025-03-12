__author__ = "8304676, Kartmann"

import argparse

def read_fasta(filename):
    sequences = []
    with open(filename, 'r') as file:
        sequence = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line
        if sequence:
            sequences.append(sequence)
    return sequences

def check_alphabet(seq1, seq2):
    alphabet1 = set(seq1)
    alphabet2 = set(seq2)
    return alphabet1 == alphabet2

def needleman_wunsch(seq1, seq2, match_score=5, mismatch_penalty=-2, gap_penalty=-6):
    n = len(seq1)
    m = len(seq2)

    # Initialisieren der Matrix
    score_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    # Erste Zeile und Spalte initialisieren
    for i in range(1, n + 1):
        score_matrix[i][0] = gap_penalty * i
    for j in range(1, m + 1):
        score_matrix[0][j] = gap_penalty * j

    # Bewertungsfunktion S(a_i, b_j)
    def score(a, b):
        if a == b:
            return match_score
        elif a == '-' or b == '-':
            return gap_penalty
        else:
            return mismatch_penalty

    # Matrix ausfüllen
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i - 1][j - 1] + score(seq1[i - 1], seq2[j - 1])
            delete = score_matrix[i - 1][j] + score(seq1[i - 1], '-')
            insert = score_matrix[i][j - 1] + score('-', seq2[j - 1])
            score_matrix[i][j] = max(match, delete, insert)

    # Backtracking
    align1, align2 = '', ''
    i, j = n, m
    while i > 0 and j > 0:
        score_current = score_matrix[i][j]
        score_diagonal = score_matrix[i - 1][j - 1]
        score_up = score_matrix[i][j - 1]
        score_left = score_matrix[i - 1][j]

        if score_current == score_diagonal + score(seq1[i - 1], seq2[j - 1]):
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1
        elif score_current == score_up + gap_penalty:
            align1 += '-'
            align2 += seq2[j - 1]
            j -= 1

    while i > 0:
        align1 += seq1[i - 1]
        align2 += '-'
        i -= 1

    while j > 0:
        align1 += '-'
        align2 += seq2[j - 1]
        j -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    return align1, align2, score_matrix

def smith_waterman(seq1, seq2, match_score=1, mismatch_penalty=-1, gap_penalty=-1):
    n = len(seq1)
    m = len(seq2)
    score_matrix = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    max_score = 0
    max_pos = (0, 0)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            match = score_matrix[i - 1][j - 1] + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty)
            delete = score_matrix[i - 1][j] + gap_penalty
            insert = score_matrix[i][j - 1] + gap_penalty
            score_matrix[i][j] = max(0, match, delete, insert)

            if score_matrix[i][j] > max_score:
                max_score = score_matrix[i][j]
                max_pos = (i, j)

    align1, align2 = '', ''
    i, j = max_pos
    while i > 0 and j > 0 and score_matrix[i][j] > 0:
        score_current = score_matrix[i][j]
        score_diagonal = score_matrix[i - 1][j - 1]
        score_up = score_matrix[i][j - 1]
        score_left = score_matrix[i - 1][j]

        if score_current == score_diagonal + (match_score if seq1[i - 1] == seq2[j - 1] else mismatch_penalty):
            align1 += seq1[i - 1]
            align2 += seq2[j - 1]
            i -= 1
            j -= 1
        elif score_current == score_left + gap_penalty:
            align1 += seq1[i - 1]
            align2 += '-'
            i -= 1
        elif score_current == score_up + gap_penalty:
            align1 += '-'
            align2 += seq2[j - 1]
            j -= 1

    align1 = align1[::-1]
    align2 = align2[::-1]

    return align1, align2, score_matrix

def print_alignment(align1, align2, score_matrix):
    print("Alignment:")
    print(align1)
    print(align2)
    print("Scoring Matrix:")
    for row in score_matrix:
        print(row)

def main():
    parser = argparse.ArgumentParser(description="Perform sequence alignment using Needleman-Wunsch and Smith-Waterman algorithms.")
    parser.add_argument("fasta_file", help="Input FASTA file with at least two sequences.")
    args = parser.parse_args()

    fasta_file = args.fasta_file
    sequences = read_fasta(fasta_file)

    if len(sequences) < 2:
        print("The FASTA file must contain at least two sequences.")
        return

    seq1, seq2 = sequences[0], sequences[1]

    if check_alphabet(seq1, seq2):
        print("Sequences have the same alphabet. Proceeding with alignment.")

        align1, align2, score_matrix = needleman_wunsch(seq1, seq2)
        print("\nNeedleman-Wunsch Alignment:")
        print_alignment(align1, align2, score_matrix)

        align1, align2, score_matrix = smith_waterman(seq1, seq2)
        print("\nSmith-Waterman Alignment:")
        print_alignment(align1, align2, score_matrix)
    else:
        print("The first two sequences do not have the same alphabet.")

if __name__ == "__main__":
    main()
