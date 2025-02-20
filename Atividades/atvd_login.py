import os 
os.system("clear") # limpar o terminal

#Solicitando dados  (entrada) 


usuario = str(input("Digite sua usúario: "))  
senha = str(input("Digite sua senha: "))  

usuario_cadastrado = "Josiel"
senha_cadastrada = "123"

#Verificando (Processamento)

if usuario_cadastrado == usuario  and senha_cadastrada == senha:
    print("ACESSO PERMITIDO")
else:
    print("ACESSO NEGADO")





#Exibindo dados (Saida)
print(" fim! ")