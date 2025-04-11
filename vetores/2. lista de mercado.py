import os
os.system("clear||clear")

lista_de_compras = []
QUANTIDADE = 3

print("= LISTA DE COMPRAS =")
for i in range(QUANTIDADE):
    item = input(f"Digite o {i+1}º item para lista: ")
    lista_de_compras.append(item)


for i, item in enumerate(lista_de_compras, start= 1):
    print(f"{i}º item: {item}")