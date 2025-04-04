import os
os.system("cls||clear")
import time

def valor_centimetro(numero):
    return numero * 100
     
    

numero = float(input("Informe o valor em metro para ser transformado em centímetro: "))

valor_total = valor_centimetro(numero) 


print(f"Calculando o valor...")
time.sleep(3)
print(f"Valor em centímetro: {valor_total}")