import numpy as np


dias = np.array(["Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado", "Domingo"])

semana_atual = np.array([28.5, 30.1, 31.4, 29.8, 27.6, 26.9, 30.0])
semana_passada = np.array([27.0, 28.5, 29.0, 30.2, 28.1, 27.5, 29.4])

fahrenheit = semana_atual * 9 / 5 + 32

media = semana_atual.mean()
maxima = semana_atual.max()
minima = semana_atual.min()
amplitude = maxima - minima

desvio_atual = semana_atual.std()
desvio_passada = semana_passada.std()

variacao = semana_atual - semana_passada
variacao_media = variacao.mean()

media_dias_uteis = semana_atual[:5].mean()
media_fim_de_semana = semana_atual[5:].mean()

diferenca_da_media = semana_atual - media

print("Temperaturas em Fahrenheit:")
for dia, temperatura in zip(dias, fahrenheit):
    print(f"{dia}: {temperatura:.2f} °F")

print()

print(f"Média: {media:.2f} °C")
print(f"Máxima: {maxima:.2f} °C")
print(f"Mínima: {minima:.2f} °C")
print(f"Amplitude: {amplitude:.2f} °C")

print()

print(f"Desvio padrão da semana atual: {desvio_atual:.2f}")
print(f"Desvio padrão da semana passada: {desvio_passada:.2f}")
if desvio_atual < desvio_passada:
    print("A semana atual foi mais estável.")
else:
    print("A semana passada foi mais estável.")

print()

print("Variação em relação à semana passada:")
for dia, valor in zip(dias, variacao):
    print(f"{dia}: {valor:+.2f} °C")

print()

print(f"Variação média em relação à semana passada: {variacao_media:+.2f} °C")
if variacao_media > 0:
    print("A semana atual foi mais quente.")
else:
    print("A semana atual foi mais fria.")

print()

print(f"Média dos dias úteis: {media_dias_uteis:.2f} °C")
print(f"Média do fim de semana: {media_fim_de_semana:.2f} °C")

print()

print("Diferença de cada dia para a média da semana:")
for dia, valor in zip(dias, diferenca_da_media):
    print(f"{dia}: {valor:+.2f} °C")
