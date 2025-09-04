import numpy as np

# Criando numPy Arrays

array = np.array(["Tenma", "Alone", "Sasha"]) # Recomendado ter elementos homogêneos embora aceite heterogêneos
                                              # Porem transforma em um mesmo tipo
print(array)
print(type(array))

matrix = np.array([["Tenma", "Alone", "Sasha"], ['Tanatos', 'Hades', 'Hipnos'],['Yuzuriha', 'Asmita', 'Sísifo']])

print(matrix, "\n")

# Funções para estruturar numPy arrays

arr = np.ones(10)
print(arr)

mtz = np.zeros(10).reshape(5,2)
print(mtz)

mtz = np.zeros((3, 4))
print(mtz)

# Arrange
arr = np.arange(10, 101)
print(arr, "\n")

print("menor valor: ", arr.min())
print("maior valor: ", arr.max())
print("media: ", arr.mean())
print("indice maior valor: ", arr.argmax(), "\n")

# Operações numPy array

arr1 = np.arange(1, 10, 1)
arr2 = np.arange(9, 0, -1)

print(arr1)
print(arr2)

# soma elemento a elemento
print(arr1 + arr2)

# Concatenando
print(np.concatenate(([arr1, arr2])))

# Operações com matriz
mtz = np.array([50,10,100,60,25,100,75,80,100]).reshape(3,3) # contas de agua luz e net de 3 meses
print(mtz, "\n")

print("Contas dos meses: ", mtz.sum(axis=1)) # 1 significa linha e 0 coluna

print("Conta de net total: ", mtz[2].sum(axis=0), "\n")

# Broadcasting
print(mtz/10, "\n")

# Numeros aleatórios
arr = np.random.randint(1, 101, 10) # 10 numeros de 1 a 100
print(arr, "\n")

# Semente aleatoria
np.random.seed(10)
arr = np.random.randint(1, 101, 10)
print(arr, "\n")

# Numeros unicos
arr = np.random.randint(1, 10, 10)
print(arr)
print(np.unique(arr, return_counts=True), "\n")