import os 
os.system ("cls||clear")

#Pedir dados


while True:
    nota = float(input("Digite sua nota: "))

    if nota < 0 or nota > 10:
        print("Nota errada \nDigite sua nota novamente.\n")
    else:
        break

while True:
    nota2 = float(input("Digite sua idade: "))

    if nota2 < 0 or nota2 > 10:
        print("Nota errada \nDigite sua nota novamente.\n")
    else:
        break

media = (nota + nota2) / 2
print(f"Média: {media}")


print("Acesso permitido")
print("FIM!")