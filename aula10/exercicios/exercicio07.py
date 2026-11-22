import numpy as np


turma_a = np.array([6.5, 7.0, 7.5, 7.0, 6.8, 7.2])
turma_b = np.array([3.0, 10.0, 9.5, 4.0, 8.0, 7.5])

for nome, turma in [("Turma A", turma_a), ("Turma B", turma_b)]:
    print(nome)
    print(f"Média: {turma.mean():.2f}")
    print(f"Maior nota: {turma.max():.2f}")
    print(f"Menor nota: {turma.min():.2f}")
    print(f"Amplitude: {turma.max() - turma.min():.2f}")
    print(f"Desvio padrão: {turma.std():.2f}")
    print()

# As médias são praticamente iguais, mas os desvios padrão são bem diferentes.
# A turma A é mais homogênea: desvio padrão e amplitude pequenos indicam
# notas próximas da média. Na turma B, as notas estão muito espalhadas.
