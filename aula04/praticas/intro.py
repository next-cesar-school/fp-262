nomes = ['Maria Eduarda', 'Carlos Vinicius', 'Marlio', 'Igor Rodinger']

i = 0
while i < len(nomes):
    print(nomes[i])
    i += 1

print('*' * 10)

for convidado in nomes:
    print(convidado)

print('*' * 10)

notas = [5, 8, 9, 6, 7, 5, 6, 8, 6, 9, 5, 8]

for nota in notas:
    print(f'- {nota} é a nota de um dos estudantes')
    print('*' * 10)
