import os
from dataclasses import dataclass
import time

# Limpa o console ao iniciar o script
os.system("cls || clear")

@dataclass
class Funcionario:
    """Classe de dados para representar um funcionário."""
    nome: str
    data_nascimento: str
    cpf: str
    funcao: str

def verificar_lista_vazia(lista_funcionarios_dados):
    """
    Verifica se a lista de funcionários está vazia.

    Args:
        lista_funcionarios_dados: A lista de funcionários a ser verificada.

    Returns:
        True se a lista estiver vazia, False caso contrário.
    """
    if not lista_funcionarios_dados:
        print("\n-----------------------------")
        print("A lista de funcionários está vazia.")
        print("-----------------------------")
        return True
    return False

def adicionar(lista_funcionario_dados):
    """
    Adiciona um novo funcionário à lista.

    Args:
        lista_funcionario_dados: A lista onde o novo funcionário será adicionado.
    """
    print("\n--- Adicionar Novo Funcionário ---")
    try:
        nome = input("Digite o nome do funcionário: ")
        # Validação simples para garantir que o nome não está vazio
        if not nome.strip():
            print("Erro: O nome não pode estar vazio.")
            return

        data_nascimento = input("Digite a data de nascimento (dd/mm/aaaa): ")
        # Adicionar validação de formato de data se necessário

        cpf = input("Digite o CPF (xxx.xxx.xxx-xx): ")
        # Adicionar validação de formato de CPF se necessário

        funcao = input("Digite a função na empresa: ")
        if not funcao.strip():
            print("Erro: A função não pode estar vazia.")
            return

        # Cria uma instância da classe Funcionario com os dados fornecidos
        novo_funcionario = Funcionario(
            nome=nome,
            data_nascimento=data_nascimento,
            cpf=cpf,
            funcao=funcao
        )
        # Adiciona o novo funcionário à lista
        lista_funcionario_dados.append(novo_funcionario)
        print("-----------------------------")
        print(f"Funcionário {novo_funcionario.nome} adicionado com sucesso!")
        print("-----------------------------")
    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o funcionário: {e}")


def mostrar(lista_funcionario_dados):
    """
    Exibe todos os funcionários cadastrados na lista.

    Args:
        lista_funcionario_dados: A lista de funcionários a ser exibida.
    """
    if verificar_lista_vazia(lista_funcionario_dados):
        return

    print("\n--- Lista de Funcionários ---")
    for i, funcionario in enumerate(lista_funcionario_dados):
        print(f"\n--- Funcionário {i + 1} ---")
        print(f"Nome: {funcionario.nome}")
        print(f"Data de Nascimento: {funcionario.data_nascimento}")
        print(f"CPF: {funcionario.cpf}")
        print(f"Função: {funcionario.funcao}")
        print("---------------------------")
    print("-----------------------------")

def remover(lista_funcionario_dados):
    """
    Remove um funcionário da lista pelo CPF.

    Args:
        lista_funcionario_dados: A lista de onde o funcionário será removido.
    """
    if verificar_lista_vazia(lista_funcionario_dados):
        return

    cpf_para_remover = input("Digite o CPF do funcionário que deseja remover: ")
    encontrado = False
    for i, funcionario in enumerate(lista_funcionario_dados):
        if funcionario.cpf == cpf_para_remover:
            removido = lista_funcionario_dados.pop(i)
            print("\n-----------------------------")
            print(f"Funcionário {removido.nome} (CPF: {removido.cpf}) removido com sucesso!")
            print("-----------------------------")
            encontrado = True
            break
    if not encontrado:
        print("\n-----------------------------")
        print(f"Funcionário com CPF {cpf_para_remover} não encontrado.")
        print("-----------------------------")


def menu_principal(lista_funcionarios_global):
    """
    Exibe o menu principal e gerencia as opções do usuário.

    Args:
        lista_funcionarios_global: A lista global de funcionários.
    """
    while True:
        print("\n--- Sistema de Gerenciamento de Funcionários ---")
        print("1. Adicionar Funcionário")
        print("2. Mostrar Funcionários")
        print("3. Remover Funcionário")
        print("4. Sair")
        print("-------------------------------------------------")

        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            adicionar(lista_funcionarios_global)
        elif escolha == '2':
            mostrar(lista_funcionarios_global)
        elif escolha == '3':
            remover(lista_funcionarios_global)
        elif escolha == '4':
            print("\nSaindo do sistema...")
            time.sleep(90)
            break
        else:
            print("\nOpção inválida. Por favor, tente novamente.")
        
        input("\nPressione Enter para continuar...")
        os.system("cls || clear")


# Lista global para armazenar os funcionários
lista_funcionarios = []

# Ponto de entrada do programa
if __name__ == "__main__":
    menu_principal(lista_funcionarios)
