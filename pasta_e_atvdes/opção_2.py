import os 
os.system("clear") # limpar o terminal

#Solicitando dados  (entrada) 


nome = str(input("Digite sue nome: "))  
idade = int(input("Digite sua idade: "))  




#Verificando (Processamento)



# OPÇÃO 2

if idade >= 18 and idade <= 65:
     print("É OGRIGADO VOTAR")
else:
    print("É OBRIGADO VOTAR")