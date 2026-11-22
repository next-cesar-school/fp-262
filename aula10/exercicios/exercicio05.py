import numpy as np


def exibir(nome, array):
    print(nome)
    print(array)
    print(f"ndim: {array.ndim} | shape: {array.shape} | size: {array.size} | dtype: {array.dtype}")
    print()


sequencia = np.arange(1, 21)
multiplos_de_5 = np.arange(0, 51, 5)
matriz_zeros = np.zeros((4, 3))
espacados = np.linspace(0, 100, 6)

exibir("Sequência de 1 a 20:", sequencia)
exibir("Múltiplos de 5:", multiplos_de_5)
exibir("Matriz de zeros:", matriz_zeros)
exibir("Valores igualmente espaçados:", espacados)

# np.arange recebe inteiros e gera inteiros.
# np.zeros e np.linspace geram float64 por padrão, porque são pensados
# para cálculos numéricos (linspace, por exemplo, quase sempre produz frações).
