import numpy as np

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [8.5, 5.6, 7.8],
    [7.5, 9.0, 9.0]
])

print(notas.mean())
print(notas.mean(axis=0))
print(notas.mean(axis=1))