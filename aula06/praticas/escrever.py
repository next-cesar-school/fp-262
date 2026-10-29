arq = open('aula06/praticas/animais.txt', 'a', encoding='utf8')

arq.write('elefante,terrestre\n')
arq.write('tambagui,aquatico\n')
arq.write('arara,aéreo\n')

lista = ['ovos\n', 'bacon\n', 'Spam\n']

arq.writelines(lista)

arq.close()
