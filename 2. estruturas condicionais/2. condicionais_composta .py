import os 
os.system("clear") # limpar o terminal

#Solicitando dados  (entrada) 
idade = int(input("Digite sua idade: ")) 

#Verificando (Processamento)
if idade < 18:
    print("Acesso negado")
else:
    print("Acesso permitido")


#Exibindo dados (Saida)
print (" fim! ")