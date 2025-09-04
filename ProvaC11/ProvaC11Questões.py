# Prova 1: Ciência de Dados com Python - Pedro Henrique Ribeiro Dias - 529
# A seguir consta a resolução de cada questão passo a passo e detalhada
import numpy as np

ds = np.loadtxt("shopping_trends.csv",
                delimiter=",",
                dtype="str",
                encoding="utf-8")

# Quetão 1: média da idade dos homems
homens = (np.char.find(ds[1:, 2], "Male") >= 0)
idadesHomens = ds[1:,1][homens].astype(int)
print(f"A média arredondada das idades dos homens é: {np.round(np.mean(idadesHomens), 0)} anos \n")

# Questão 2: Quantidade de clientes que gastaram mais do que a média de gastos
gastos = ds[1:,5].astype(float)
mediaGastos = np.mean(gastos)
acimaDaMedia = (gastos > mediaGastos) # Posicoes onde o gasto é maior do que a media de gastos

print(f"A quantidade de clientes que gastaram mais do que média é: {np.sum(acimaDaMedia)} \n")

# Questão 3: Porcetagem de vendas do item menos vendido
itensVendidos = ds[1:, 3]
itens, contagem = np.unique(itensVendidos, return_counts=True) # Itens unicos e numreo de suas aparicoes nas vendas

itemMenosVendido = itens[np.argmin(contagem)]
numVendas = np.sum(itensVendidos == itemMenosVendido) # Numero de vendas do item menos vendido

print(f"A porcetagem de vendas do item menos vendido é: {np.round(numVendas/len(itensVendidos), 4) *100}% \n")

# Questão 4: Porcentagem de vendas com desconto
desconto = ds[1:, 13]
descontosAplicados = np.sum(desconto == "Yes")
print(f"A porcetagem de vendas com desconto aplicado é: {np.round(descontosAplicados/len(desconto), 4) *100}% \n")

# Questão 5: Qual a cor de roupa mais popular do verão
cores = ds[1:, 8]
estacoes = ds[1:, 9]

coresVerao = cores[estacoes == "Summer"]

cor, contagem = np.unique(coresVerao, return_counts=True) # Cores Unicas e numero de suas aparições nas vendas
corMaisPopular = cor[np.argmax(contagem)]

print(f"A cor de roupa mais popular do verão é: {corMaisPopular} \n")