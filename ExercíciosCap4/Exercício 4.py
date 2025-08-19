import numpy as np
import random

matriz = np.random.randint(1,10,(random.randint(1,10), random.randint(1,10)))

linhas, colunas = matriz.shape

elementos = linhas * colunas

print("A matriz tem: ", elementos, " elementos")

if elementos%2 == 0:
    print("Matriz unidimensional com um numero par de elementos")
else:
    print("Matriz unidimensional com um numero impar de elementos")