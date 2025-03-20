import os 
os.system ("cls||clear")

#Pedir dados
idade = int(input("Digite sua idade: "))

while idade < 18:
    print("Não autorizado \nSomente maiores de 18.\n")
    idade = int(("Digite sua idade: "))
print("Acesso permitido.")
print("FIM!")