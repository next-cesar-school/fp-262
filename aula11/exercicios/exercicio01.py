import numpy as np


notas = np.array([4.5, 7.0, 8.5, 5.0, 9.0, 6.5])

aprovadas = notas >= 7
recuperacao = (notas >= 5) & (notas < 7)
reprovadas = notas < 5

print("Notas maiores ou iguais a 7:", notas[aprovadas])
print("Notas entre 5 e 6.9:", notas[recuperacao])
print("Notas menores que 5:", notas[reprovadas])
print("Quantidade de estudantes aprovados:", aprovadas.sum())
