import os
os.system("cls || clear")
from dataclasses import dataclass


@dataclass
class Endereco:
    logradouro: str
    numero: int
    cidade: str 

@dataclass
class Pessoa:
    nome: str
    email: str
    endereco: Endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.email}")
        print(f"Endereço: {self.endereco.logradouro}, Número: {self.endereco.numero}, Cidade: {self.endereco.cidade}")

endereco1 = Endereco("Rua A", 23, "Salvador")
pessoa1 = Pessoa("Marta", "gifbib@gmail.com", endereco1)
pessoa1.exibir_dados()

print()
endereco2 = Endereco("Rua B", 47, "Salvador")
pessoa2 = Pessoa("Maria", "fkonwo@gmail.com", endereco2)
pessoa2.exibir_dados()
