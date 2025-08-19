# Aula 1 - colecoes (exemplo com cavaleiros do zodiaco lost canvas)

# Coleção segura usada para puxar dados
tuplaCDZ = ('Tenma', 'Sasha', 'Albafica', 'Manigold', 'El cid')

# Printando elementos
print(tuplaCDZ)

# Alterando elementos
# tuplaCDZ[1] = 'Alone' - nao funcionará, a coleção é imutável

# Slicing de elementos
print(tuplaCDZ[2:4]) # Albafica e Manigold - o primeiro argumento é inclusivo e o segundo exclusivo

print(tuplaCDZ[3:]) # El cid e Manigold

print(tuplaCDZ[-2]) # Manigold com indice negativo

# Funcoes prontas
print(len(tuplaCDZ)) # Tamanho
print(max(tuplaCDZ)) # Tabela Ascii - ordem alfabetica
print(min(tuplaCDZ)) # Tabela Ascii - ordem alfabetica

# Listas

listaCDZ = ['Yuzuriha', 'Alone', 'Asmita', 'Sísifo']

print(listaCDZ)

# Adicionando elementos
listaCDZ.append('Hakurei') # Adiciona no fim da lista
listaCDZ.insert(1, 'Yati') # adiciona no indice desejado

print(listaCDZ)

# Alterando elementos
listaCDZ[1] = 'Yato'

# Excluindo elementos
del listaCDZ[1] # remocao por indice
listaCDZ.remove('Yuzuriha') # remocao por valor
print(listaCDZ)

# Conjuntos

# Conjunto não guarda a ordem dos elementos
conjuntoCDZ = {'Minos de Grifo',
               'Rhadamanthys de Wyvern',
               'Aiacos de Garuda',
               'Kagaho de Benu',
               'Violate de Behemoth',
               'Serpentário'}

print(conjuntoCDZ)

# Adicionando elemento
conjuntoCDZ.add('Youma de Mephistopheles')
conjuntoCDZ.add('Youma de Mephistopheles') # Nao adiciona elementos repetidos
print(conjuntoCDZ)

# Remover elementos
conjuntoCDZ.remove('Serpentário')
print(conjuntoCDZ)

# Como descobrir o tipo de algo
print(type(conjuntoCDZ))

# Dicionários

dicionarioCDZ = {
                 'nome':'Hipnos',
                 'idade':'indefinido',
                 'sexo':'Masculino'
                }

print(dicionarioCDZ)

# Adicionando
dicionarioCDZ['raca'] = 'Deus'
dicionarioCDZ['Familia'] = ['Tanatos', 'Oneiros', 'Icelos', 'Fantasos', 'Morpheus']

# Update
dicionarioCDZ['idade'] = 50

# Delete
del dicionarioCDZ['idade']

print(dicionarioCDZ)

# Acessando o Tanatos
print(dicionarioCDZ['Familia'][0])