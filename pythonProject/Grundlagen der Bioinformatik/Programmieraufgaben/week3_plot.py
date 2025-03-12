import matplotlib.pyplot as plt
import numpy as np

# Daten der bereits berechneten Distanzen
hamming_distances = np.array([0, 0.15, 0.35, 0.6, 0.75])
jukes_kantor_distances = np.array([0, 0.17, 0.47, 1.21, np.nan])
kimura_distances = np.array([0, 0.17, 0.49, np.nan, np.nan])

# Plotten der Ergebnisse
plt.figure(figsize=(8, 6))
plt.plot(hamming_distances, jukes_kantor_distances, 'o-', label='Jukes-Kantor')
plt.plot(hamming_distances, kimura_distances, 's-', label='Kimura-2-Parameter')
plt.xlabel('Hamming-Distanz')
plt.ylabel('Korrigierte Distanz')
plt.legend()
plt.grid(True)
plt.title('Vergleichende korrigierte Distanzen')
plt.show()
