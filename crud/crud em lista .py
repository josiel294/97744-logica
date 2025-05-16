    # CRUD em lista
import os 
from dataclasses import dataclass
os.system("cls || clear")


# Criando uma lista para nomes.

lista_nomes = []


# Create - Adicionar / Inserir
nome = "Marta"
lista_nomes.append(nome)
print(f"O nome {nome} foi inserido com sucesso.")

#################################################


print("\nRead - Ler / Mostrar")
print(lista_nomes)

print("\nUpdate - Atualizar/Alterar")
nome_para_atualizar = "Marta"
if  nome_para_atualizar in lista_nomes: 
    nome_novo = "Marta Silva"
    indice = lista_nomes.index(nome_para_atualizar)
    lista_nomes[indice] = nome_novo
    print(f"O nome {nome_para_atualizar}")
else:
    print(f"O nome {nome_para_atualizar}")


print(lista_nomes)

########################################

print("\nDelete - Excluir")
nome_para_excluir = "Marta"
if nome_para_excluir in lista_nomes:
    lista_nomes.remove(nome_para_excluir)
    print(f"O nome {nome_para_excluir} foi excluido com sucesso.")
else:
    print(f"O nome {nome_para_excluir} não foi encontrado.")

    print(lista_nomes)