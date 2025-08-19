import numpy as np
import random
campoMinado = np.zeros(4).reshape(2,2)

tentativas = 0

campoMinado[random.randint(0,1)][random.randint(0,1)] = 1

linha = int(input("Insira o valor da linha que deseja visitar: "))
coluna = int(input("Insira o valor da coluna que deseja visitar: "))

while True:
    if campoMinado[linha][coluna] == 1:
        print("Game Over! :( Try it again!")
        break
    elif campoMinado[linha][coluna] == 0:
        campoMinado[linha][coluna] = 0
        print("vivo!")
        tentativas += 1

    if tentativas == 3:
        print("Congratulations! You beat the game!")
        break

    linha = int(input("Insira o valor da linha que deseja visitar: "))
    coluna = int(input("Insira o valor da coluna que deseja visitar: "))