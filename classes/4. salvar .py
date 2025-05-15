import os
from dataclasses import dataclass
os.system("cls||clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: str
    matricula: str
    endereco: str

@dataclass
class Cliente:
    nome: str
    data_nascimento: str
    endereco: str

lista_funcionario = []
lista_cliente = []

QUANTIDADES_LISTAS = 3


for i in range(QUANTIDADES_LISTAS):
    print("Dadaos dos funcionarios")
    funcionario = Funcionario(
    nome = input("Digite seu nome: "),
    data_admissao = input("Digit a data de admissão(xx/xx/xxxx): "),
    matricula = input("Digite o número da matricula: "),
    endereco = input("Digite o seu endereço: ")
    
    )
    lista_funcionario.append(funcionario)


for i in range(QUANTIDADES_LISTAS):
    print("Dados dos clientes")
    cliente = Cliente(
    nome = input("Digite o seu nome: "),
    data_nascimento = input("Digita data de seu nascimento(xx/xx/xxxx): "),
    endereco = input("Digite o seu endereço: ")
    )

    lista_cliente.append(cliente)

for funcionario in lista_funcionario:
    print(f"Nome: {funcionario.nome}")   
    print(f"Data de Nascimento: {funcionario.data_admissao}")   
    print(f"Data de Nascimento: {funcionario.matricula}")   
    print(f"Endereço: {funcionario.endereco}")   
    print()


for cliente in lista_cliente:
    print(f"Nome: {cliente.nome}")   
    print(f"Data de Nascimento: {cliente.data_nascimento}")   
    print(f"Endereço: {cliente.endereco}")   
    print()

nome_arquivo_func = "dados_funcionario.csv"
nome_arquivo_cli = "dados_cliente.csv"

print("= Salvando os dados dos arquivos =")

# 'w' -> escrita/salvar/sobrescrever
with open(nome_arquivo_func, "a") as arquivo:
    for funcionario in lista_funcionario:
        arquivo.write(f"{funcionario.nome}, {funcionario.data_admissao}, {funcionario.matricula} e {funcionario.endereco}\n")

with open(nome_arquivo_cli, "a") as arquivo:
    for cliente in lista_cliente:
        arquivo.write(f"{cliente.nome}, {cliente.data_nascimento}, {cliente.endereco}\n")

print("\nSalvo com sucesso!")