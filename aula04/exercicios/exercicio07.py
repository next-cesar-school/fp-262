limite = int(input('Digite o numero : '))
primos = []
a = 2
while (a <= limite):
    resto = 0
    for x in range(2,a):
        if (a % x == 0):
            resto += 1

    if resto == 0:
        primos.append(a)
    a += 1
print(primos)
