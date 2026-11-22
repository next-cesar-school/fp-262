import numpy as np


precos = np.array([100, 250, 80, 300, 150])

precos_com_desconto = precos * 0.9

print("Preços originais:", precos)
print("Preços com desconto:", precos_com_desconto)
print("Maior preço original:", precos.max())
print("Menor preço com desconto:", precos_com_desconto.min())

'''
#alternativa mais didática
import numpy as np


precos = np.array([100, 250, 80, 300, 150])

desconto = precos * 0.10
precos_com_desconto = precos - desconto

print("Preços originais:", precos)
print("Descontos:", desconto)
print("Preços com desconto:", precos_com_desconto)
print("Maior preço original:", precos.max())
print("Menor preço com desconto:", precos_com_desconto.min())
'''