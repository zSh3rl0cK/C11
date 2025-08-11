estoqueLoja1 = {'Samsung', 'Nokia', 'Motorola', 'Iphone'}

estoqueLoja2 = {'Samsung', 'Xiaomi', 'Iphone', 'LG'}

estoqueGeral = estoqueLoja1.union(estoqueLoja2)

print("Modelos disponiveis no total: ", estoqueGeral)
print("Modelos Loja 1: ", estoqueLoja1)
print("Modelos Loja 2: ", estoqueLoja2)