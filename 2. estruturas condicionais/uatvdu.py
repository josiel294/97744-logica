import os
os.system("clear")

#solocitar dados
numero_um = int(input("Digite o primeiro numero: "))
numero_dois = int(input("Digite o segundo numero: "))
numero_tres = int(input("Digite o terceiro numero: "))


#processamento

maior = max (numero_um, numero_dois, numero_tres)
menor = min (numero_um, numero_dois, numero_tres)





#exibir dados
print(f"Maior numero: ", {maior})
print(f"Menor numero: ", {menor})
