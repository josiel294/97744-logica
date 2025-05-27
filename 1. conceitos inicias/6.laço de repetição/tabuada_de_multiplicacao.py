import os
os.system("cls || clear")
import time


numero = int(input("Digite um número para ver a tabuada: "))

# Exibe a tabuada de 1 a 10
print(f"\nTabuada de {numero}:")

for i in range(1, 11):
   print(f"{numero} x {i} = {numero * i}")
   time.sleep(1)
