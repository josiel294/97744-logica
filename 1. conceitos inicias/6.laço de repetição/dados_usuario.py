import os
os.system("cls || clear")


soma = 0
# Solicitar ao usuário um número
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: ")) 
    soma += numero
print(f"\nA soma dos números informados é: {soma}")