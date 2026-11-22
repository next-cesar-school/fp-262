import numpy as np


notas = np.array([
    [8.0, 7.5, 9.0],
    [6.5, 8.0, 7.0],
    [9.5, 8.5, 10.0],
    [5.0, 6.0, 6.5]
])

media_geral = notas.mean()
media_por_estudante = notas.mean(axis=1)
media_por_avaliacao = notas.mean(axis=0)
maior_nota = notas.max()
menor_nota = notas.min()

print("Média geral:", media_geral)
print("Média de cada estudante:", media_por_estudante)
print("Média de cada avaliação:", media_por_avaliacao)
print("Maior nota da matriz:", maior_nota)
print("Menor nota da matriz:", menor_nota)
