import os

import numpy as np


pasta = os.path.dirname(os.path.abspath(__file__))
caminho_entrada = os.path.join(pasta, "consumo_energia.csv")
caminho_saida = os.path.join(pasta, "resumo_consumo.csv")

consumo = np.loadtxt(caminho_entrada, delimiter=",")

casas = np.array([f"Casa {i}" for i in range(1, consumo.shape[0] + 1)])

total_por_casa = consumo.sum(axis=1)
media_por_mes = consumo.mean(axis=0)
total_por_mes = consumo.sum(axis=0)
indice_mes_maior_consumo = np.argmax(total_por_mes)
casas_acima_200 = casas[consumo.mean(axis=1) > 200]

print("Formato dos dados:", consumo.shape)

print()

print("Consumo total por casa:")
for casa, total in zip(casas, total_por_casa):
    print(f"{casa}: {total:.0f} kWh")

print()

print("Consumo médio por mês:")
for mes, media in enumerate(media_por_mes, start=1):
    print(f"Mês {mes}: {media:.2f} kWh")

print()

print(f"Mês com maior consumo total: Mês {indice_mes_maior_consumo + 1} ({total_por_mes[indice_mes_maior_consumo]:.0f} kWh)")
print("Casas com consumo médio acima de 200 kWh:", ", ".join(casas_acima_200))

np.savetxt(caminho_saida, total_por_casa, delimiter=",", fmt="%.0f", header="total_kwh", comments="")
print(f"\nResumo salvo em {caminho_saida}")
