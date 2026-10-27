# Filtrar de elementos de uma lista
# criar uma nova lista apenas com os itens com 5 caracteres ou menos

nomes_original = ['Miguel', 'Arthur', 'Heitor', 'Helena', 'Alice', 'Laura', 'Gabriel', 'Davi', 'Maria Clara', 'Pedro', 'Yoda', 'Caio']
nomes_selecionados = []

for nome in nomes_original:
    if len(nome) <= 5:
        nomes_selecionados.append(nome)

print(nomes_selecionados)
