import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Bewertungsfunktion
def scoring_function(a, b):
    if a == b:
        return 5  # Match
    elif a == '-' or b == '-':
        return -6  # Gap
    else:
        return -2  # Mismatch

# Funktion zum Berechnen der Smith-Waterman-Matrix und der Traceback-Matrix
def smith_waterman(seq1, seq2):
    n = len(seq1) + 1
    m = len(seq2) + 1

    F = np.zeros((n, m), dtype=int)
    traceback = np.zeros((n, m), dtype=str)

    max_score = 0
    max_pos = (0, 0)

    for i in range(1, n):
        for j in range(1, m):
            match = F[i-1][j-1] + scoring_function(seq1[i-1], seq2[j-1])
            delete = F[i-1][j] + scoring_function(seq1[i-1], '-')
            insert = F[i][j-1] + scoring_function('-', seq2[j-1])
            F[i][j] = max(0, match, delete, insert)

            if F[i][j] == match:
                traceback[i][j] = '↖'
            elif F[i][j] == delete:
                traceback[i][j] = '↑'
            elif F[i][j] == insert:
                traceback[i][j] = '←'
            else:
                traceback[i][j] = '0'

            if F[i][j] > max_score:
                max_score = F[i][j]
                max_pos = (i, j)

    return F, traceback, max_score, max_pos

# Funktion zum Rekonstruieren des optimalen lokalen Alignments
def reconstruct_local_alignment(traceback_matrix, seq1, seq2, start_pos):
    alignment1 = []
    alignment2 = []
    alignment_path = []
    i, j = start_pos

    while traceback_matrix[i][j] != '0' and i > 0 and j > 0:
        alignment_path.append((i, j))
        if traceback_matrix[i][j] == '↖':
            alignment1.append(seq1[i-1])
            alignment2.append(seq2[j-1])
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == '↑':
            alignment1.append(seq1[i-1])
            alignment2.append('_')
            i -= 1
        elif traceback_matrix[i][j] == '←':
            alignment1.append('_')
            alignment2.append(seq2[j-1])
            j -= 1

    alignment_path.append((i, j))  # Add the starting point
    return ''.join(reversed(alignment1)), ''.join(reversed(alignment2)), alignment_path

# Beispielsequenzen
seq1 = "AATTACA"
seq2 = "AGATAGA"

# Berechnen der Matrix und Traceback-Matrix
F, traceback, max_score, max_pos = smith_waterman(seq1, seq2)

# Rekonstruieren des optimalen lokalen Alignments
alignment1, alignment2, alignment_path = reconstruct_local_alignment(traceback, seq1, seq2, max_pos)

# Ausgabe des optimalen Alignments und Scores
print("Optimal Local Alignment 1: ", alignment1)
print("Optimal Local Alignment 2: ", alignment2)
print("Optimal Local Alignment Score: ", max_score)
print("Traceback Path: ", alignment_path)

# Funktion zur Darstellung der Matrix mit Backtrace-Pfad
def plot_matrix_with_arrows(score_matrix, traceback_matrix, title, seq1, seq2, alignment_path=None):
    fig, ax = plt.subplots()
    cax = ax.matshow(score_matrix, cmap='Blues')
    plt.title(title)
    fig.colorbar(cax)
    ax.set_xticks(np.arange(len(seq2)+1))
    ax.set_yticks(np.arange(len(seq1)+1))
    ax.set_xticklabels([''] + list(seq2))
    ax.set_yticklabels([''] + list(seq1))
    plt.xlabel('Seq2')
    plt.ylabel('Seq1')

    # Annotate the matrix with the scores and directions
    for (i, j), val in np.ndenumerate(score_matrix):
        ax.text(j, i, f'{val}', ha='center', va='center', color='black')
        if traceback_matrix[i, j] == '↖':
            ax.arrow(j, i, -0.4, -0.4, head_width=0.1, head_length=0.1, fc='red', ec='red')
        elif traceback_matrix[i, j] == '↑':
            ax.arrow(j, i, 0, -0.5, head_width=0.1, head_length=0.1, fc='red', ec='red')
        elif traceback_matrix[i, j] == '←':
            ax.arrow(j, i, -0.5, 0, head_width=0.1, head_length=0.1, fc='red', ec='red')

    if alignment_path:
        for (i, j) in alignment_path:
            ax.plot(j, i, 'ro')

    plt.show()

# Plot the score matrix with arrows and the alignment path
plot_matrix_with_arrows(F, traceback, 'Smith-Waterman Score Matrix with Traceback and Alignment Path', seq1, seq2, alignment_path)
