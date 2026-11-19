import numpy as np

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0]
])

pesos = np.array([2, 3, 5])

notas_ponderadas = notas * pesos
print(notas_ponderadas)

media_ponderada = notas_ponderadas.sum(axis=1) / pesos.sum()
print(media_ponderada)