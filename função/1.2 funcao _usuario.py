import os 
os.system("cls||clear")


#função sem retorno
#Dedinindo característica da função
def saudacao(nome):
    print(f"Olá {nome}! Bem-vindo ao curso de DS!")


nome = input("Digite seu nome: ")
nome_da_disciplina = input("Digite o nome da sua disciplina: ") 


# criar uma função
def disciplina(nome):
    print(f"Você faz parte da disciplina {nome} que faz parte do curso de DS!")


saudacao(nome) # Chamndo a função 
disciplina(nome_da_disciplina)