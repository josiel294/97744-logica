import os
from datetime import datetime
os.system("cls||clear")


def caulcular_idade(ano_nascimento):
    return datetime.now().year - ano_naascimento

ano_naascimento = int(input("Digite o ano do seu nascimento: "))

idade = caulcular_idade(ano_naascimento)

print(f"Idade: {idade}")