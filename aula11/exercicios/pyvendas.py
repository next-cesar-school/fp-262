import numpy as np


def formatar_lista(nomes):
    if len(nomes) == 0:
        return "nenhum vendedor"

    return ", ".join(nomes)


vendedores = np.array(["Ana", "Bruno", "Carlos", "Duda"])

dias = np.array(["Segunda", "Terça", "Quarta", "Quinta", "Sexta"])

vendas = np.array([
    [1200, 1500, 1100, 1800, 2000],
    [900,  1000, 950,  1200, 1300],
    [2000, 2100, 1900, 2200, 2500],
    [700,  850,  800,  950,  1000]
])

total_por_vendedor = vendas.sum(axis=1)
total_por_dia = vendas.sum(axis=0)
media_por_vendedor = vendas.mean(axis=1)

indice_maior_vendedor = np.argmax(total_por_vendedor)
indice_maior_dia = np.argmax(total_por_dia)

vendedores_acima_7000 = vendedores[total_por_vendedor > 7000]

print("Total vendido por vendedor:")
for vendedor, total in zip(vendedores, total_por_vendedor):
    print(f"{vendedor}: R$ {total:.2f}")

print()

print("Total vendido por dia:")
for dia, total in zip(dias, total_por_dia):
    print(f"{dia}: R$ {total:.2f}")

print()

print("Média de vendas por vendedor:")
for vendedor, media in zip(vendedores, media_por_vendedor):
    print(f"{vendedor}: R$ {media:.2f}")

print()

print(f"Vendedor com maior total de vendas: {vendedores[indice_maior_vendedor]}")
print(f"Total vendido: R$ {total_por_vendedor[indice_maior_vendedor]:.2f}")

print()

print(f"Dia com maior venda total: {dias[indice_maior_dia]}")
print(f"Total do dia: R$ {total_por_dia[indice_maior_dia]:.2f}")

print()

print("Vendedores que venderam mais de R$ 7000.00:", formatar_lista(vendedores_acima_7000))
