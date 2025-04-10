import os 
os.system("cls||clear")


#função sem retorno
#Dedinindo característica da função
def saudacao(nome):
    print(f"Olá {nome}! Bem-vindo ao curso de DS!")

# criar uma função
def disciplinalgp(nome):
    print(f"Você faz parte da disciplina {nome} que faz parte do curso de DS!")


nome_visitante = "Marta"
nome_da_disciplina = "Lógica de progamação"
saudacao(nome_visitante) # Chamndo a função 
disciplinalgp(nome_da_disciplina)