numero = float(input("Digite um número "))

intervalo1 = int(input("Digite o inicio do intervalo "))
intervalo2 = int(input("Digite o final do intervalo"))

for c in range(intervalo1, intervalo2):
    print(c*numero)