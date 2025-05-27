import os 
os.system("clear") # limpar o terminal

#Solicitando dados  (entrada) 


nome = str(input("Digite sue nome: "))  
idade = int(input("Digite sua idade: "))  




#Verificando (Processamento)



if idade < 18 or idade > 65:
    print("NÃO É OBRIGADO VOTAR")
if idade > 16 and idade < 17 or  65:
    print("VOTO OPCIONAL")
if idade > 18 and idade < 65:
    print("É OBRIGADO VOTAR")
