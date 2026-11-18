import numpy as np

notas = np.array([7.5, 8.0, 6.5, 9.0])

print(notas[0])
print(notas[-1])

print(notas[:2])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0]
])

print(notas)
print(notas[0, 0])
print(notas[2, 1])
print(notas[2])
print(notas[:, 2])
