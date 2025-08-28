import numpy as np

ds = np.loadtxt("paises.csv",
                delimiter=";",
                dtype="str",
                encoding="utf-8") # especificamente esse dataset é utf 8

print(f"{ds[0]} \n")

# Questão 1: Mostrando apenas as colunas: País, região, população e area
print(f"{ds[1:,:3]} \n")

# Questão 2: Contando e mostrando os diferentes países
unicos = np.unique(ds[1:, 1])
print(f"Quantidade de paises: {len(unicos)} \n")
print(f"{np.unique(ds[1:, 1])} \n")

# Questão 3: Mostrando a taxa média de alfabetização
print(f"A taxa média de alfabetização é: {np.round(np.mean(ds[1:,9].astype(float)), 4)}% \n")

# Questão 4: Contando o número de países da america do norte
paises = ds[1:,1]
print(f"{len(paises[np.char.find(ds[1:,1], "NORTHERN AMERICA") >= 0])} paises da america do norte\n")

# Questão 5: Qual país da america do sul e carib possuem maior renda per capita
# paises = (ds[1:,1] == "LATIN AMER. & CARIB") tentativa nao funcional

paisesSAM = (np.char.find(ds[1:,1], "LATIN AMER. & CARIB") >= 0)
renda =  ds[1:,8].astype(float)
rendaMax = np.max(renda[paisesSAM])

pais = (renda == rendaMax) & paisesSAM
print(f"Renda max: {rendaMax} \n Pais com renda máxima: {ds[1:,0][pais]} \n")