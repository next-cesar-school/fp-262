import numpy as np

notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0])

aprovados = notas >= 7

print(notas[aprovados])

print(notas[notas >= 7])

print(notas >= 7)
print((notas >= 7).sum())

print(notas[(notas >= 5) & (notas <= 8)])
print(notas[(notas < 5) | (notas > 8)])