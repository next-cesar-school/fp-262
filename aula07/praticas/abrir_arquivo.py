arquivo = None

try:
    arquivo = open('dados.txt', 'r', encoding='utf-8')
    conteudo = arquivo.read()
except FileNotFoundError:
    print('Erro: Arquivo não encontrado.')
else:
    print('Arquivo lido com sucesso!')
finally:
    if arquivo is not None:
        print('Fechando arquivo')
        arquivo.close()
    print('Encerrando operação.')
