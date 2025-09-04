import numpy as np

ds = np.loadtxt("space.csv",
                delimiter=";",
                dtype="str",
                encoding="utf-8") # especificamente esse dataset é utf 8
# Questão 4
spacex = (ds[1:, 1] == "SpaceX")
custo = ds[1:, 6].astype(float)

valorMaxSpacex = np.max(custo[spacex])
print(valorMaxSpacex)
idxsMaxsSpacex = custo[spacex] == valorMaxSpacex

print(ds[1:,0:][spacex][idxsMaxsSpacex])

idxValorMaxSpacex = np.argmax(custo[spacex])
print(idxValorMaxSpacex)
print((ds[1:, 1:])[idxValorMaxSpacex])