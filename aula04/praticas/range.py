# Uso do range
range(10)           # 0 até 9
range(-10, 10)      # -10 até 9
range(-10, 10, 2)   # -10 até 9, de 2 em 2 (-10, -8, -6, -4, ..., 6, 8)

#print(list(range(-10, 10, 2)))

# repetir num número x de vezes
'''for _ in range(10):
    print('Olha eu me repetindo...')'''

# receber 4 notas de um estudante e adicionar a uma lista

'''notas = []
for _ in range(4):
    valor = float(input('Insira uma das notas: '))
    notas.append(valor)

print(notas)'''

# exibir todos os números pares contidos de 1 a 100

for num in range(1, 101):
    if num % 2 == 0:
        print(num)

print('🐐' * 5)

for num in range(2, 101, 2):
    print(num)
