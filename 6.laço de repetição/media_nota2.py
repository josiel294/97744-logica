import os
os.system("cls || clear")


divisao = 0
# Solicitar ao usuário um número
for i in range(3):
    media = float(input(f"Digite sua {i + 1}º nota: ")) 
    divisao += media
    media_total = divisao / 3
    print()
if media_total >= 7:
    print("Aluno Aprovado!")
if media_total <=4:
    print("Aluno Reprovado!")

print(f"\nA sua media é: {media_total: .2f}")