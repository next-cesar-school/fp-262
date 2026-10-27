texto = input('Insira um texto aqui: ')

#'um exemplo de texto' -> ['u', 'm', ' ', 'e', 'x'...]

for letra in texto:
    print(letra)

for palavra in texto.split(','):
    print(palavra)
