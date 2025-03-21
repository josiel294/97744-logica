import os 
os.system ("cls||clear")

#Pedir dados


while True:
    nota = int(input("Digite sua idade: "))

    if nota < 0 or nota > 10:
        print("Nota errada \nDigite sua nota novamente.\n")
    else:
        break

print("Acesso permitido")
print("FIM!")