import numpy as np

notas = np.loadtxt('aula11\\praticas\\notas.csv', delimiter=',')

print(notas)

medias = notas.mean(axis=1)

np.savetxt('aula11\\praticas\\medias.csv', medias, delimiter=',', fmt='%.2f', header='media', comments='')
