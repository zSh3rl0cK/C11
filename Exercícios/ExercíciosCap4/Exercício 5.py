import numpy as np

np.random.seed(10)
matriz = np.random.randint(1, 51, size=(4,4))

print(matriz, "\n")

# Número de linhas e colunas
linhas, colunas = matriz.shape

# Médias corretas
print("Média das linhas: ", matriz.mean(axis=1))
print("Média das colunas: ", matriz.mean(axis=0), "\n")

# Maior média
print("Maior média (linha): ", matriz.mean(axis=1).max())
print("Maior média (coluna): ", matriz.mean(axis=0).max(), "\n")

# Valores únicos e contagens
valores, contagens = np.unique(matriz, return_counts=True)
print("Valores únicos: ", valores)
print("Contagem de cada valor: ", contagens, "\n")