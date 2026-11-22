import numpy as np


produtos = np.array(["Teclado", "Mouse", "Monitor", "Cadeira", "Webcam", "Headset"])
precos = np.array([150, 80, 1200, 900, 250, 350])
estoque = np.array([25, 5, 8, 12, 3, 40])

repor = estoque < 10
prioridade = (precos > 500) & (estoque < 10)
promocao = (precos < 100) | (estoque > 30)

valor_total = (precos * estoque).sum()

print("Precisam de reposição:", produtos[repor])
print("Prioridade de reposição:", produtos[prioridade])
print("Candidatos a promoção:", produtos[promocao])
print("Não precisam de reposição:", produtos[~repor])
print(f"Valor total em estoque: R$ {valor_total:.2f}")
