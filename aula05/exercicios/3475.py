# -*- coding: utf-8 -*-


def fala_numero(numero):
    extenso = ['zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove']

    if numero.isdecimal():
        print(extenso[int(numero)])
    else:
        print(extenso.index(numero))

n = input()
fala_numero(n)
