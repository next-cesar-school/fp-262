# Tópicos a explorar
# - Criando um dicionário

palavras = {'dog': ('cão', 'cachorro'),
            'bird': 'pássaro',
            'lion': 'leão',
            0: 'zero',
            1.1: 'um e mais um pouquinho'}

# - Acessando elementos de um dicionário

print(type(palavras), palavras)
print(palavras['lion'])
print(palavras['dog'])
print(palavras[0])

# - Adição de itens por atribuição

palavras['tiger'] = 'tigre'

print(palavras)

# - Adição de itens por update

adicao = [('crocodile', 'crocodilo'), ('monkey', 'macaco')]

palavras.update(adicao)

print(palavras)

# - Removendo itens

palavras.pop('crocodile')
palavras.popitem()

print(palavras)

# - esvaziando um dicionário

#palavras.clear()
#del(palavras)
print(palavras)

# Tópicos a explorar
# - adicionar valores + update()
# - get()
#print(palavras['elephant'])
print(palavras.get('lion', 'Elemento não encontrado'))

# - keys()
print(palavras.keys())

# - values()
print(palavras.values())

# - items()
print(palavras.items())

# - for
for elemento in palavras.items():
    print(elemento)

for eng, port in palavras.items():
    print(f'Chave: {eng} - Valor: {port}')
