import os 
os.system ("cls||clear")

#Pedir dados

while True:
    idade = int(input("Digite sua idade: "))

    if idade < 18:
        print("Não autorizado \nSomente maiores de 18.\n")
    else:
        break

print("Acesso permitido")
print("FIM!")
        