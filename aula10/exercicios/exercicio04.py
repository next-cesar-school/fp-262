import numpy as np


lista = [1, 2, 3]
array = np.array([1, 2, 3])

# Previsões:
# lista * 2       -> [1, 2, 3, 1, 2, 3]  (repete a lista)
# array * 2       -> [2 4 6]             (multiplica cada elemento)
# lista + lista   -> [1, 2, 3, 1, 2, 3]  (concatena as listas)
# array + array   -> [2 4 6]             (soma posição com posição)

print(lista * 2)
print(array * 2)
print(lista + lista)
print(array + array)

# Mesmo resultado de array * 2 usando apenas listas
dobro = []
for valor in lista:
    dobro.append(valor * 2)

print(dobro)
