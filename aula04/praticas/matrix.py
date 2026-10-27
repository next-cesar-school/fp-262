# Iterando sobre matriz
# listas dentro de listas

matriz = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

for linha in matriz:
    print(f'-> {linha}')
    for item in linha:
        print(item)
print(linha)
print(item)
