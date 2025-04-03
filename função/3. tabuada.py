import os
os.system("cls||clear")


def tabuada(numero):
    print(f"\nTabuada {numero}" )
    for i in range(1,11):
        print(f"{numero} x {i} = {numero * i}")

numero_da_tabuada = int(input("Digite o número que deseja: "))

tabuada(numero_da_tabuada)
