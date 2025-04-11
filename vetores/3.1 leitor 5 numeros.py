import os
os.system("cls||clear")


lista_de_numeros = []
QUANTIDADE = 5

def maior_menor(lista):
    maior = max (lista)
    menor= min (lista)
    return maior, menor

def solicitar_dados():
    for i in range(QUANTIDADE):
        numero = float(input("Digite o número: "))
        lista_de_numeros.append(numero)
    return lista_de_numeros

def mostra_dados():
    for i, numero in enumerate(lista_de_numeros, start= 1):
        print(f"Número {i}º numero: {numero}")
    
    print(f"Maior número: {maior}")
    print(f"Menor número: {menor}")

solicitar_dados()
maior, menor = maior_menor(lista_de_numeros)
mostra_dados()
