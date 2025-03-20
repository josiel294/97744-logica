import os 
os.system ("cls||clear")

#Pedir dados


while True:
    nota = float(input("Digite sua primeira nota: "))

    if nota < 0 or nota > 10:
        print("Nota errada \nDigite sua nota novamente.\n")
    else:
        break

while True:
    nota2 = float(input("Digite sua segunda nota: "))

    if nota2 < 0 or nota2 > 10:
        print("Nota errada \nDigite sua nota novamente.\n")
    else:
        break
while True:
    nota3 = float(input("Digite sua terceira nota: "))

    if nota3 < 0 or nota3 > 10:
        print("Nota errada \nDigite sua nota novamente.\n")
    else:
        break
media = (nota + nota2 + nota3) /3

while True:
    if media >= 7:
        print("Aluno aprovado!")
        break
    elif 5 <= media < 7:
        print("Aluno em recuperação.")
        break
    else:
        print("Aluno reprovado.")
        break
print(f"Média: {media: .2f}")


print("FIM!")