while(True):
  nota = float(input('Insira uma nota entre 0 e 10: '))

  if 0 <= nota <= 10:
    break
  else:
    print('Nota inválida. Tente novamente')
