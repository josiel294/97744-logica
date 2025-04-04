import os
os.system("cls||clear")


def caulcular_idade(ano_nascimento):
    return 2025 - ano_naascimento

ano_naascimento = int(input("Digite a data do seu nascimento: "))

idade = caulcular_idade(ano_naascimento)

print(f"Idade: {idade}")