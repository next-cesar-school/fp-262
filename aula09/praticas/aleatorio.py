import random

letras = ['a', 'b', 'c', 'd', 'e']

'''for _ in range(10):
    print(random.randint(1, 10))'''

print(random.choices(letras, k=2))

random.shuffle(letras)
print(letras)
