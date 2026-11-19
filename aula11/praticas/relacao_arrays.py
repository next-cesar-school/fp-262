import numpy as np

nomes = np.array(['Ana', 'Bruno', 'Carlos', 'Duda', 'Eva'])
notas = np.array([4.5,    7.0,     8.5,      5.0,    9.0])

print(nomes[notas >= 7])

print(notas.max())
print(np.argmax(notas))

pos_maior_nota = np.argmax(notas)

print(nomes[pos_maior_nota], notas[pos_maior_nota])

pos_menor_nota = np.argmin(notas)

print(nomes[pos_menor_nota], notas[pos_menor_nota])

vendas = np.array([
    [1200, 1500, 1100],
    [900,  1000, 1300]
])

print(np.argmax(vendas, axis=1))
