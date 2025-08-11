pessoas = {}

maiorPeso = 0
nomeMaiorPeso = ""
menorPeso = 300
nomeMenorPeso = ""

for c in range(1, 4):
    nome = input('Digite seu nome: ')
    peso = float(input('Digite seu peso: '))
    pessoas[nome] = peso

    if peso > maiorPeso:
        maiorPeso = peso
        nomeMaiorPeso = nome

    if peso < menorPeso:
        menorPeso = peso
        nomeMenorPeso = nome

print("O nome de quem tem o maior peso é", nomeMaiorPeso, "com", maiorPeso , "kg")
print("O nome de quem tem o menor peso é", nomeMenorPeso, "com", menorPeso, "kg")
