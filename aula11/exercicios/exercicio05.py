import numpy as np


cidades = np.array(["Recife", "Olinda", "Caruaru", "Petrolina", "Garanhuns"])
dias = np.array(["Seg", "Ter", "Qua", "Qui", "Sex"])

temperaturas = np.array([
    [30.5, 31.0, 29.8, 32.1, 31.4],
    [30.0, 30.8, 29.5, 31.6, 31.0],
    [27.2, 28.0, 26.9, 29.0, 28.4],
    [33.8, 34.5, 35.2, 34.0, 33.1],
    [24.0, 25.1, 23.8, 26.4, 25.0]
])

media_por_cidade = temperaturas.mean(axis=1)
media_por_dia = temperaturas.mean(axis=0)

indice_mais_quente = np.argmax(media_por_cidade)
indice_mais_fria = np.argmin(media_por_cidade)
indice_dia_mais_quente = np.argmax(media_por_dia)
dia_maximo_por_cidade = np.argmax(temperaturas, axis=1)

print("Temperatura média por cidade:")
for cidade, media in zip(cidades, media_por_cidade):
    print(f"{cidade}: {media:.2f} °C")

print()

print(f"Cidade mais quente: {cidades[indice_mais_quente]} ({media_por_cidade[indice_mais_quente]:.2f} °C)")
print(f"Cidade mais fria: {cidades[indice_mais_fria]} ({media_por_cidade[indice_mais_fria]:.2f} °C)")
print(f"Dia mais quente da semana: {dias[indice_dia_mais_quente]} ({media_por_dia[indice_dia_mais_quente]:.2f} °C)")

print()

print("Dia de maior temperatura em cada cidade:")
for cidade, indice_dia in zip(cidades, dia_maximo_por_cidade):
    print(f"{cidade}: {dias[indice_dia]}")
