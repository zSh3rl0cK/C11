sexo = input("Digite seu sexo (F ou M): ").upper()

while sexo != "F" and sexo != "M":
    sexo = input("Valor inválido. Digite seu sexo (F ou M): ").upper()

if sexo == "F":
    print("Uau, uma mulher")

if sexo == "M":
    print("Uau, um homem")
    