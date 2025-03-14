import os
os.system("cls || clear")
import time

contagem = int(input("Digíte quantos segundos deseja: "))


print(f"\nContagem regressiva pares:{contagem} ")
for i in range (contagem, 0, -1):
    print(f"contagem: {i} ")
    time.sleep(1)

print("Acabou")