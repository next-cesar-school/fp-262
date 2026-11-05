numeros = set()

numeros.add(1)
numeros.add(2)
numeros.add(3)
numeros.add(1)
numeros.add(2)
numeros.add(1)
numeros.add(4)
numeros.add(1)
numeros.add(1)

print(numeros)

lista_ingredientes = ['bacon', 'banana', 'spam', 'ovos', 'spam', 'salsicha', 'spam']
unicos_ingredientes = set(lista_ingredientes)

print(unicos_ingredientes)

convidados = {'thiago', 'carlos', 'eduarda', 'Thiago', 'eduarda dourado'}

print(convidados)

print('carlos' in convidados)

convidados.remove('eduarda')

for nome in convidados:
    print(f'- {nome}')
