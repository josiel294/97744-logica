import os
os.system("cls || clear")


divisao = 0
# Solicitar ao usuário um número
for i in range(4):
    media = float(input(f"Digite sua {i + 1}º nota: ")) 
    divisao += media
    media_total = divisao / 4
print(f"\nA soma dos números informados é: {media_total: .2f}")