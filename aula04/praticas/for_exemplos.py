frutas = ['maçã', 'banana', 'laranja', 'uva', 'ração', 'desodorante']

i = 0
while i < len(frutas):
    item = frutas[i]
    print(item)
    i += 1

print('*'*10)

for fruta in frutas:
    print(f'Item da lista -> {fruta}')

print('*'*10)

# exibir apenas as idades maiores que 35
idades = [19, 45, 30, 35, 33, 13, 67, 22]

for idade in idades:
    if idade > 35:
        print(idade)

print('*'*10)

# Iteração sobre uma string
nome_completo = input('Insira o seu nome completo: ')

# cada letra será um elemento
for letra in nome_completo:
    print(letra)

# Cada palavra como elemento
for palavra in nome_completo.split():
    print(palavra)

# Uso do range
# repetir num número x de vezes
#print(list(range(10)))
#print(list(range(5, 10)))
for _ in range(10):
    print('eita')

# receber 4 notas de um estudante e adicionar a uma lista
notas = []

quant_notas = int(input('Quantas notas você quer ler? '))

for _ in range(quant_notas):
    nota = float(input('Insira uma nota: '))
    notas.append(nota)

media = sum(notas)/len(notas)
print(media)

# exibir todos os números pares contidos de 1 a 100
for num in range(1, 101):
    if num % 2 == 0:
        print(num)

for num in range(2, 101, 2):
    print(num)

# Iterando sobre matriz
# listas dentro de listas

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for elemento in matriz:
    for item in elemento:
        print(item)
    print('-------')

print(matriz[2][1])
print(len(matriz))

# Filtrando de elementos de uma lista
# criar uma nova lista apenas com os itens com 5 caracteres ou menos

nomes_original = ['Miguel', 'Arthur', 'Heitor', 'Helena', 'Alice', 'Laura', 'Gabriel', 'Davi', 'Maria Clara', 'Pedro', 'Yoda', 'Caio']
nomes_selecionados = []

for nome in nomes_original:
    if len(nome) <= 5:
        nomes_selecionados.append(nome)

print(nomes_selecionados)
