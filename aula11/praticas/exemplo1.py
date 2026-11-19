import numpy as np

nomes = np.array(['Ana', 'Bruno', 'Carlos', 'Duda'])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 6.0, 5.0]
])

medias = notas.mean(axis=1)
print(medias)

aprovados = medias >= 7
print(aprovados)

print(nomes[aprovados])
print(medias[aprovados])

recuperacao = (medias >= 5) & (medias < 7)

print(nomes[recuperacao])
print(medias[recuperacao])

reprovado = medias < 5

print(nomes[reprovado])
print(medias[reprovado])
