import os
os.system("clear")

#solocitar dados
numero_um = int(input("Digite o primeiro numero: "))
numero_dois = int(input("Digite o segundo numero: "))



#processamento

if numero_um > numero_dois:
    maior = numero_um
    menor = numero_dois
else:
    maior = numero_um
    menor = numero_dois




#exibir dados
print(f"Maior numero: ", {maior})
print(f"Menor numero: ", {menor})
