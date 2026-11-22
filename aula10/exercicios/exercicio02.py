import numpy as np


notas = np.array([6.0, 7.5, 8.0, 5.5, 9.0])

notas_corrigidas = notas + 0.5

print("Notas originais:", notas)
print("Notas corrigidas:", notas_corrigidas)
print("Média antes da correção:", notas.mean())
print("Média depois da correção:", notas_corrigidas.mean())
