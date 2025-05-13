import os
from dataclasses import dataclass

os.system('cls || clear') 

@dataclass
class Paciente:
    nome:str
    idade:int



lista_de_pacientes = []

for i in range(2):
    print("digite os dados do paciente:")
    paciente = Paciente(
        nome= input("Nome:"),
        idade= int(input("Idade:"))

    )
    lista_de_pacientes.append(paciente)
    print()

nome_arquivo = "dados_pacientes.csv"

print("salvando dados no arquivo.")
with open(nome_arquivo, "a") as arquivo_pacientes:
    for paciente in lista_de_pacientes:
        arquivo_pacientes.write(f"{paciente.nome},{paciente.idade} \n")
print("salvo com sucesso.")

print("\nAcessando dados em arquivo .")
try:
    with open(nome_arquivo, "r") as arquivo_pacientes:
        linhas = arquivo_pacientes.readlines()
        for linha in linhas:
            print(f"- {linha.strip()}")
except FileNotFoundError:
    print("o arquivo nao foi encontrado.")