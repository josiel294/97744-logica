import os
os.system("cls || clear")
import time

print("Contagem regressiva: ")
for i in range (10, 0, -1):
    print(f"Segundos:{i} ")
    time.sleep(1)

print("Acabou")