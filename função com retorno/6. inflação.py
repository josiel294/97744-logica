import os
os.system("clear||cls")
import time

def inflacao(preco):
    if preco < 100:
        valor = preco * 1.10
    else:
        valor = preco * 1.20
    return valor

preco = float(input("Digite o valor do seu produto: "))


valor_total = inflacao(preco)

print(f"Valor total será R$: {valor_total}")