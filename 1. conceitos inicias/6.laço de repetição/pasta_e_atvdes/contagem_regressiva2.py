import os
os.system("cls || clear")
import time

# Solicitar o número ao usuário
numero = int(input("Digite um número para a contagem regressiva: "))

# Fazer a contagem regressiva
while numero >= 0:
    print(numero)
    time.sleep(1)  # Aguardar 1 segundo
    numero -= 1

print("Contagem regressiva finalizada!")
