import numpy as np


notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [5.0, 6.0, 6.5]
])

pesos = np.array([2, 3, 5])

notas_ponderadas = notas * pesos
medias_ponderadas = notas_ponderadas.sum(axis=1) / pesos.sum()

print("Notas ponderadas:")
print(notas_ponderadas)

print("Médias ponderadas:", medias_ponderadas)
