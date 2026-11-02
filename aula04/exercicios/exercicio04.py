vetor = []

for i in range(10):
  numero_do_usuario = int(input())
  vetor.append(numero_do_usuario)

valor_maximo = max(vetor)
posicao_do_valor_maximo = vetor.index(valor_maximo)

print(f'Valor máximo: {valor_maximo}; Posição: {posicao_do_valor_maximo}')
