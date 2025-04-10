import os
os.system("cls||clear")
import time

def verificar (numero):
    if numero > 0:
        print("Número é positivo")
    elif numero < 0:
        print("Número é negativo")
    else:
        print("Número é neutro")

numero = int(input("Digite o número: "))
print("Verificando o número....")
time.sleep(2)
verificar(numero)

