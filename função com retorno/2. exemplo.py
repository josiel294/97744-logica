import os
os.system("cls||clear")


def somar(n1, n2):
    calcular = n1 + n2
    return calcular


def subtrair(n1, n2):
    calcular = n1 - n2
    return calcular

def multiplicar(n1, n2):
    return  n1 * n2 

def dividir(n1, n2):
    calcular = n1 / n2
    return calcular

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))



soma = somar (n1, n2)
multiplicacao = multiplicar (n1, n2)
divisao = dividir (n1, n2)
subtracao = subtrair (n1, n2)

print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")
print(f"Divisão: {divisao: .2f}")
print(f"Subtração: {subtracao}")