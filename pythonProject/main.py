import numpy as np

# PAM1 Übergangswahrscheinlichkeits-Matrix (angenommene Werte)
# Die Matrix sollte eigentlich aus realen Daten kommen, hier sind nur beispielhafte Werte
PAM1 = np.array([
    [0.987, 0.002, 0.002, 0.002, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001],
    [0.002, 0.988, 0.002, 0.002, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001],
    [0.002, 0.002, 0.988, 0.002, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001],
    [0.002, 0.002, 0.002, 0.987, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.989, 0.002, 0.002, 0.002, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.002, 0.989, 0.002, 0.002, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.002, 0.002, 0.989, 0.002, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.002, 0.002, 0.002, 0.989, 0.001, 0.001],
    [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.989, 0.002],
    [0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.001, 0.002, 0.989],
])

# Effektive Häufigkeit der 20 Aminosäuren (angenommene Werte)
frequencies = np.array([
    0.082, 0.015, 0.054, 0.066, 0.045, 0.056, 0.065, 0.073, 0.025, 0.072,
    0.058, 0.026, 0.092, 0.041, 0.048, 0.051, 0.067, 0.055, 0.059, 0.066
])

# Aminosäuren-Index
amino_acids = "ACDEFGHIKLMNPQRSTVWY"

# Funktion zur Berechnung des PAM1 Scores
def calculate_pam_score(seq1, seq2):
    score = 0.0
    for a, b in zip(seq1, seq2):
        i = amino_acids.index(a)
        j = amino_acids.index(b)
        p_ij = PAM1[i, j]
        f_i = frequencies[i]
        f_j = frequencies[j]
        score += np.log(p_ij / (f_i * f_j))
    return round(score, 2)

# Beispiel-Sequenzen
seq1 = "MYYGK"
seq2 = "TTYGH"

# Berechnung des Alignment-Scores
score = calculate_pam_score(seq1, seq2)
print("Alignment Score:", score)
