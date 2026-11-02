while(True):
  usuario = input('Nome de usuário: ')
  senha = input('Senha: ')

  if usuario == senha:
    print('Você não pode definir o nome de usuário igual a senha!')
  else:
    break
