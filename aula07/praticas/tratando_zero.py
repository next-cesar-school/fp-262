def divisao(a, b):
    return a / b

try:
    num1 = int(input('Insira o 1º número: '))
    num2 = int(input('Insira o 2º número: '))

    resultado = 0

    resultado = divisao(num1, num2)


except ZeroDivisionError as e:
    print('ERRO: Você tentou dividir um número por Zero')
    print(f'Descrição do Erro: {e}')
    resultado = None
except (ValueError, NameError, EOFError):
    print('ERRO: Algo de errado com a conversão dos tipos!')
else:
    print(f'Resultado: {resultado}')
finally:
    ...
