idade = int(input("Digite sua idade: "))
nome = input("Digite seu nome: ")

print(nome.upper())
print(nome.lower())

print(nome.count("") - nome.count(" "))
nomes = nome.split()
nomes[-1] = ("do inatel")
nomes = " ".join(nomes)
print(nomes)