import os
os.system("cls||clear")



def calcular(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


nota1 = float(input("Digite sua nota: "))
nota2 = float(input("Digite sua nota: "))

media_total = calcular(nota1, nota2)

if media_total > 7:
    print("Aluno Aprovado!")
else:
    print("Aluno Reprovado!")






    