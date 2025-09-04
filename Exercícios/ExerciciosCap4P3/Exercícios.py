import numpy as np

ds = np.loadtxt("space.csv",
                delimiter=";",
                dtype="str",
                encoding="utf-8") # especificamente esse dataset é utf 8

# Questão 1
mtz = ds[1:, 7] # Matriz formada pelos status da missao pulando a linha do cabeçalho
print(f"A porcentagem de sucessos é: {np.round(((np.sum(mtz == "Success"))/len(mtz))*100,4)}% \n")

# Questão 2
mtz = ds[1:, 6].astype(float) # Matriz formada pelas linhas com o custo de cada missão
print(f"A média de custo para missões com valores (>0) é: {np.round(np.sum(mtz[mtz > 0])/(np.sum(mtz > 0)),2)} \n")

# Questão 3
mtz = ds[1:, 2] # Matriz formada pelas linhas dos locais de cada missão
print(f"Missões realizadas pelos EUA: {np.sum(np.char.find(mtz, 'USA') >= 0)} \n") # poderia usar apenas count tbm

# Questão 4
spacex = (ds[1:, 1] == "SpaceX")
custo = ds[1:, 6].astype(float)

max_custo = np.max(custo[spacex])  # valor máximo de custo
mask_max = (custo == max_custo) & spacex  # missões da SpaceX que têm esse custo máximo

print(f"As missões mais caras da empresa SpaceX custaram: {max_custo} milhões \n")
for linha in ds[1:][mask_max]:
    print(linha)

# Questão 5
empresas = np.unique(ds[1:, 1])   # nomes únicos
for empresa in empresas:
    print(f"A empresa {empresa} realizou {np.sum(ds[1:, 1]  == empresa)} missões")