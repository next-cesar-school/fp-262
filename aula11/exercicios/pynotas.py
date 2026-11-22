import numpy as np


def formatar_lista(nomes):
    if len(nomes) == 0:
        return "nenhum estudante"

    return ", ".join(nomes)


nomes = np.array([
    "Ana",
    "Bruno",
    "Carlos",
    "Duda",
    "Eduardo",
    "Fernanda"
])

notas = np.array([
    [8.0, 7.5, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 9.5],
    [4.0, 6.0, 5.0],
    [7.0, 7.0, 7.0],
    [5.0, 4.5, 6.0]
])

medias = notas.mean(axis=1)
media_por_avaliacao = notas.mean(axis=0)
media_geral = notas.mean()

aprovados = medias >= 7
recuperacao = (medias >= 5) & (medias < 7)
reprovados = medias < 5

indice_maior_media = np.argmax(medias)
indice_menor_media = np.argmin(medias)

print("Médias dos estudantes:")
for nome, media in zip(nomes, medias):
    print(f"{nome}: {media:.2f}")

print()

print("Média por avaliação:")
for indice, media in enumerate(media_por_avaliacao, start=1):
    print(f"Avaliação {indice}: {media:.2f}")

print()

print(f"Média geral da turma: {media_geral:.2f}")

print()

print("Aprovados:", formatar_lista(nomes[aprovados]))
print("Recuperação:", formatar_lista(nomes[recuperacao]))
print("Reprovados:", formatar_lista(nomes[reprovados]))

print()

print(f"Maior média: {nomes[indice_maior_media]} ({medias[indice_maior_media]:.2f})")
print(f"Menor média: {nomes[indice_menor_media]} ({medias[indice_menor_media]:.2f})")
