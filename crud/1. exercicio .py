import os
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    nascimento: str
    cpf:str
    funcao: str

def verificar_lista_vazia(lsita):
    if not list:
        print("\nA lista está vazia.")
        return True
    return False

def adicionar (lista):
    print("Adicionar funcionario")





lista_funcionarios = []
for i in range(1):
    adicionar(lista_funcionarios)

mostrar_funcionarios(lista_funcionarios)