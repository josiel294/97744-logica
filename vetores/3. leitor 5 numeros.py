import os
os.system("cls||clear")

lista_de_numeros = []
QUANTIDADE = 5

for i in range(QUANTIDADE):
    numero = float(input("Digite o número: "))
    lista_de_numeros.append(numero)

maior_numero = max (lista_de_numeros)
menor_numero = min (lista_de_numeros)

print(f"Maior número: {maior_numero}")
print(f"Menor número: {menor_numero}")


for i, numero in enumerate(lista_de_numeros, start= 1):
    print(f"Número {i}º numero: {numero}")