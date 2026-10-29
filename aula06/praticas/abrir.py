arq = open('aula06/praticas/exemplo.txt', encoding='utf8')


print(arq.read())

arq.seek(0)

print(arq.readline())
print(arq.readline())
print(arq.readline())

arq.seek(0)

print(arq.read())

arq.seek(0)

print(arq.readlines())

arq.seek(0)

for linha in arq:
    print(f'{len(linha) - 1} - {linha}')
