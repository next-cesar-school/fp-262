with open('aula06/praticas/animais.txt', encoding='utf8') as bichos:
    cont_terrestres = 0
    for linha in bichos:
        if 'terrestre' in linha:
            cont_terrestres += 1

    print(f'Quant. de animais terrestres: {cont_terrestres}')

with open('aula06/praticas/notas.txt', 'a') as arq_notas:
    quant_estudantes = int(input('Quantos estudantes? '))
    for _ in range(quant_estudantes):
        nome = input('Qual o nome do estudante: ')
        notas = []
        for n in range(4):
            notas.append(float(input(f'Insira a nota {n + 1}: ')))

        arq_notas.write(f'{nome},{notas[0]},{notas[1]},{notas[2]},{notas[3]}\n')
