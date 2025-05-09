import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Cliente:
    nome: str
    email: str
    telefone: str

lista_clientes = []

QUANTIDADES_CLIENTES = 2


for i in range (QUANTIDADES_CLIENTES):
    cliente = Cliente( #instanciando um objeto 
        nome = input("Nome: "),  #adicionar virgula menos no ultimo 
        email = input("Email: "), 
        telefone = input("Telefone: ")

    )
    lista_clientes.append(cliente)
    print()

print("\n= Exibindo dados clientes =")
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")
    print(f"Nome: {cliente.email}")
    print(f"Nome: {cliente.telefone}")
    print()

print("= Salvando os dados dos arquivos =")
nome_arquivo = "dados_clientes"

# w -> escrita/salvar/sobrescrever
# a -> escrita/salvar/acumular

with open(nome_arquivo, "a") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.nome}, {cliente.email}, {cliente.telefone}\n")

print("\nSalvo com sucesso!")
