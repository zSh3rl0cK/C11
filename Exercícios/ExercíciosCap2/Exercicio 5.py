numero = input("Digite um número entre 1000 e 9999: ")

# Verifica se o número tem 4 dígitos e é numérico
while not (len(numero) == 4):
    numero = input("Entrada inválida. Digite um número com exatamente 4 dígitos: ")

print("Milhar:", numero[0])
print("Centena:", numero[1])
print("Dezena:", numero[2])
print("Unidade:", numero[3])
