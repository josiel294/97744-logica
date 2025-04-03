import os
os.system("cls||clear")

soma_das_notas = 0
contador = 0

while True:
    nota = float(input("Digite sua nota: "))


    soma_das_notas += nota
    contador += 1

    mais_notas = input("Deseja adicionar mais uma nota? S/N: ").lower()
    if mais_notas == "n":
        break
if contador >0:
    media = soma_das_notas / contador
    print("Media total: {media: .2f}")
else: 
    print("nenhuma nota foi foi informada")
