import os
os.system("cls||clear")


soma = 0
contador = 0

while True:
    numero = int(input("Digite o número inteiro positivo (ou um valor negativo para encerrar a operação): "))


    if numero <0:
        print("Progama encerrado.")
        break
    


    soma += numero
    contador += 1


    if contador >0:
        media = soma / contador
        print(f"Resultado da média aritimética: {media:.2f}")
    else:
        print("Nenhum número desejado encontrado.")