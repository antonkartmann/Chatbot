import matplotlib.pyplot as plt
import numpy as np

# Die beiden Polypeptidsequenzen
seq1 = "MGPVKTYGPV"
seq2 = "GPVKTYPVKVPG"

# Erstellen einer leeren Matrix für den Dotplot
dotplot = np.zeros((len(seq1), len(seq2)))

# Füllen der Matrix
for i in range(len(seq1)):
    for j in range(len(seq2)):
        if seq1[i] == seq2[j]:
            dotplot[i, j] = 1

# Zeichnen des Dotplots
plt.imshow(dotplot, cmap='Greys', interpolation='none')

# Hervorheben von diagonalen Übereinstimmungen (längere identische Bereiche)
for i in range(len(seq1) - 1):
    for j in range(len(seq2) - 1):
        if dotplot[i, j] == 1 and dotplot[i + 1, j + 1] == 1:
            plt.plot([j, j + 1], [i, i + 1], color='red')  # Markiere diagonale Übereinstimmungen in rot

plt.xlabel('GPVKTYPVKVPG')
plt.ylabel('MGPVKTYGPV')
plt.title('Dotplot der Polypeptide')
plt.xticks(ticks=range(len(seq2)), labels=list(seq2))
plt.yticks(ticks=range(len(seq1)), labels=list(seq1))
plt.grid(True)
plt.show()

# Analyse des Dotplots:
# Rote Linien zeigen diagonale Übereinstimmungen, die längere identische Bereiche zwischen den beiden Sequenzen
# darstellen.
# Diese diagonalen Linien weisen auf Abschnitte hin, in denen die Sequenzen übereinstimmen.
# Wiederholende oder ähnliche Muster in beiden Sequenzen werden durch diese diagonalen Linien dargestellt.


