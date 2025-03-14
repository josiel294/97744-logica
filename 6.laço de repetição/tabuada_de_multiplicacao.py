import os
os.system("cls || clear")

# Solicitar ao usuário um número
numero = int(input("Digite um número para ver sua tabuada: "))

# Exibir a tabuada do número
print(f"\nTabuada do {numero}:")
for i in range(1, 11):  # Vai de 1 até 10
    print(f"{numero} x {i} = {numero * i}")
