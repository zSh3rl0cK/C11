kilometros = float(input("Digite a distancia da sua viagem"))
if kilometros <= 200:
    preco = kilometros*0.50
    print("O preço a ser pago é: ", preco)

else:
    preco = kilometros*0.45
    print("O preço a ser pago é: ", preco)
    