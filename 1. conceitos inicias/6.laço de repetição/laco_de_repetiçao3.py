import os

os.system("cls || clear")

print("Contagem de 100 até 120 \nApenas pares: ")
for i in range (100, 121, 2):
    if i % 2 == 0:
        print(f"Numero:{i} ")