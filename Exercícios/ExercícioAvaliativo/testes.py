import numpy as np

ds = np.loadtxt("paises.csv",
                delimiter=";",
                dtype="str",
                encoding="utf-8") # especificamente esse dataset é utf 8

# Questão 4: Contando o número de países da america do norte
regioes = ds[1:,1]
paises = ds[1:,0]
print(f"{len(regioes[np.char.find(ds[1:,1], "NORTHERN AMERICA") >= 0])} paises da america do norte\n")

print(f"{paises[np.char.find(ds[1:,1], "NORTHERN AMERICA") >= 0]}")

# Questão 5: Qual país da america do sul e carib possuem maior renda per capita
paisesSAM = (np.char.find(ds[1:,1], "LATIN AMER. & CARIB") >= 0)

# Teste 2
continentes = np.char.strip(ds[1:, 1])  # remove espaços em branco nas bordas
paisesSAM2 = (continentes == "LATIN AMER. & CARIB")

print(f"{continentes}")

print(f"{ds[1:,0][paisesSAM2]}")

# Resolução passo a passo

nomesPaisesSAM = paises[paisesSAM]
rendas = ds[1:,8].astype(float)
rendasPaisesSam = rendas[paisesSAM]
rendasPaisesSAMmax = np.argmax(rendasPaisesSam)
nomePaisRendaMaxSam = nomesPaisesSAM[rendasPaisesSAMmax]
print(f"{nomePaisRendaMaxSam}")

print(f"{np.max(rendasPaisesSam)}")

print(f"{ds[1:,0][paisesSAM][np.argmax(ds[1:,8].astype(float)[paisesSAM])]} \n")

