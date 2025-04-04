import os 
os.system("cls||clear")
import time

def somar (n1,n2):
    return n1 + n2

def dividir (somar):
    return somar / 2

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))

soma = somar(n1,n2)
media = dividir(soma)


print(f"Calculando o valor total da média...")
time.sleep(2)
print(f"Valor total da media dos número: {media: .2f}")
