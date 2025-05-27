import os
os.system("cls || clear")

# Inicializa a variável para armazenar a soma
soma = 0

# Solicita ao usuário 5 números inteiros
for i in range(5):
    numero = int(input(f"Digite o {i + 1}º número: "))  # Solicita cada número
    soma += numero  # Adiciona o número à soma

# Exibe a soma total
print(f"\nA soma dos números informados é: {soma}")
