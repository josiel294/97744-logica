import os
os.system("cls || clear")

impares = 0
pares = 0
# Solicitar ao usuário um número
for i in range(5):
    numero = int(input(f"Digite o {i+ 1}º número: ")) 
    if i % 2 == 0:
       pares += 1
    else:
       impares += 1
       
print(f"Pares:{pares}")
print(f"Impares:{impares}")