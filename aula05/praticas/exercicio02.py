'''
[Exercício 02]
Crie um programa que tenha uma função que receba uma lista de números inteiros e
exiba todos os valores multiplicados por um valor inserido pelo usuário.
'''

def multiplica_lista(numeros):
    multiplicador = int(input('Insira o valor multiplicador: '))

    for numero in numeros:
        print(numero * multiplicador)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
multiplica_lista(nums)

def recebe_notas(quant_notas):
    notas = []
    for _ in range(quant_notas):
        notas.append(float(input('Insira uma nota: ')))

    multiplicador = int(input('Insira o multiplicador das notas: '))

    for nota in notas:
        print(nota * multiplicador)

recebe_notas(2)