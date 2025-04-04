import os
os.system("cls||clear")

import time


def contar_par_impares():
    pares = 0
    impares = 0

    for i in range(6):
        numero =  int(input(f"Digite o {i+ 1}º número: ")) 
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

quantidade_pares, quantidade_impares =contar_par_impares()

print("Verificando os dados...")
time.sleep(2)
print(f"Quantidades de pares: {quantidade_pares}")
print(f"Quantidades de ímpares: {quantidade_impares}")






