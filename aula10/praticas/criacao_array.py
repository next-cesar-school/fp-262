import numpy as np

idades = np.array([18, 21, 25, 30])

#numeros = range(0, 10, 2)
numeros = np.arange(0, 10, 2)

print(numeros)

zeros = np.zeros(10)
uns = np.ones(10)

print(zeros)
print(uns)

matriz = np.zeros((3, 4))
print(matriz)

valores = np.linspace(0, 1, 5)
print(valores)

print(matriz.ndim)
print(matriz.shape)
print(matriz.size)
print(matriz.dtype)
print(idades.dtype)
