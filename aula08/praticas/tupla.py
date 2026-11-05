lista_dias = ['domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado']
tupla_dias = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')

print(type(lista_dias))
print(type(tupla_dias))

valores = [110123423213, 4445212235785]
coordenadas = tuple(valores)
del(valores)

print(coordenadas, type(coordenadas))

#coordenadas[0] = 3245 # dá erro!

print(tupla_dias[0])
print(tupla_dias[-1])
print(tupla_dias[1:6])

print(tupla_dias.index('terça'))

print(len(tupla_dias))

numeros = 1, 2, 3, 4

print(numeros)

def acai(*complementos):
    print(type(complementos), complementos)

acai('aaa', 'bbbb', 'cccc')
