import os
os.system ("cls||clear")

quantidade_de_pares = 0
quantidade_de_impares = 0
contador = 0
soma_geral = 0
soma_pares = 0

while True:
    numero = float(input("Digite o número: "))

    if numero == 0:
        break

    if numero % 2 == 0:
        quantidade_de_pares += 1
        soma_pares += numero
    else:
        quantidade_de_impares +=1

    soma_geral += numero
    contador += 1

if contador > 0:
    media_pares = soma_pares / quantidade_de_pares
    media_geral = soma_geral / contador

    print(f"Quantidade dos números pares: {quantidade_de_pares}")
    print(f"Quantidade dos números ímpares : {quantidade_de_impares}")
    print(f"Quantidade da media dos números pares: {media_pares:.2f}")
    print(f"Quantidade da media dos números geral: {media_geral:.2f}")
else:
    print("\nNão foram informados os números necessários para a operação.")
    
