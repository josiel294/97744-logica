import os
os.system("cls||clear")

QUANTIDADE = 6
quantidade_numero = []

def contar_pares_impares(numeros):
    pares = 0
    impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    return pares, impares

def solicitar_dados():
    for i in range(QUANTIDADE):
        numero = int(input(f"Digite o {i+1}º número: "))
        quantidade_numero.append(numero)

def mostrar_dados(numeros, pares, impares):
    print("\nNúmeros digitados:")
    for i, numero in enumerate(numeros, start=1):
        print(f"{i}: {numero}")
    print(f"\nNúmeros pares: {pares}")
    print(f"Números ímpares: {impares}")

# Execução do programa
solicitar_dados()
pares, impares = contar_pares_impares(quantidade_numero)
mostrar_dados(quantidade_numero, pares, impares)
