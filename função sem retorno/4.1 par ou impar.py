import os
os.system("cls||clear")
import time

def verificar(numero):
    if numero % 2 == 0:
        print("O número é par")
    else:
        print("O número é impar")


numero = int(input("Digite um número: "))
print("Verificando se o número é par ou ímpar.")
time.sleep(2)
verificar(numero)