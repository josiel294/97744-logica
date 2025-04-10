import os
os.system("cls||clear")

pares = 0
impares = 0

def verificar_par_impar (numero):
    if numero % 2 == 0:
        print(f"O número {numero} número é par ")
    else:
        print(f"O número {numero} número é ímpar")

verificar_par_impar(7)
verificar_par_impar(10)