pessoas = []  # lista para guardar cada pessoa

# Escrevendo um dicionario com cada pessoa e guardando na lista
for i in range(1, 21):
    pessoa = {
        "Nome": input("Digite o nome da pessoa: "),
        "Idade": int(input("Digite a idade da pessoa: ")),
        "Sexo": input("Digite o sexo da pessoa (M/F): ").upper()
    }
    pessoas.append(pessoa)

# Média de idades
mediaIdades = sum(p["Idade"] for p in pessoas) / len(pessoas)
print("A idade média é:", mediaIdades)

# Contar mulheres com menos de 20 anos
mulheresJovens = sum(1 for p in pessoas if p["Sexo"] == "F" and p["Idade"] < 20)
print("O N° de mulheres com menos de 20 é", mulheresJovens)
