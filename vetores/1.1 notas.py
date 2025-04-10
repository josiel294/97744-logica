import os
os.system("cls||clear")

notas = []
QUANTIDADE_NOTAS = 4

for i in range(QUANTIDADE_NOTAS):
    nota = float(input("Digite sua nota: "))
    notas.append(nota)

media = sum(notas) / QUANTIDADE_NOTAS

print()
if nota >=7:
    resultado = "Aprovado"
elif nota >= 5:
    resultado = "Recuperação"
else:
    resultado = "Reprovado"

for nota in notas:
    print(f"Notas: {nota}")

print()
print(f"Media: {media: .2f}")
print()
print(f"Situação: {resultado}")

