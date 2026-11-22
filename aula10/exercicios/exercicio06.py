import numpy as np


temperaturas = np.array([29.5, 30.2, 31.0, 28.7, 27.9, 32.4, 33.1])

print("Quarta-feira:", temperaturas[2])
print("Três primeiros dias:", temperaturas[:3])
print("Fim de semana:", temperaturas[-2:])
print("Dias úteis:", temperaturas[:5])
print("Dias alternados:", temperaturas[::2])

print()

turnos = np.array([
    [26.0, 31.5, 27.0],
    [24.5, 29.0, 25.5],
    [28.0, 34.0, 29.5]
])

print("Segunda cidade:", turnos[1])
print("Temperaturas da tarde:", turnos[:, 1])
print("Noite na terceira cidade:", turnos[2, 2])
