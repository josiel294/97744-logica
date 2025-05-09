import os 
from dataclasses import dataclass
import time
os.system ("cls || clear")


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

print("\nExebindo dados cliente: ")
time.sleep(2)
for cliente in lista_clientes:
    print(f"Nome: {cliente.nome}")   
    print(f"Emeail: {cliente.email}")   
    print(f"Telefonee: {cliente.telefone}")   
    print()