import os
os.system("clear || cls")

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


@dataclass
class Pet:
    nome: str
    idade: int
    peso: float

#Exemplo de uso da classe

pessoa1 = Pessoa ("Alice", 30)
pessoa2 = Pessoa ("Bob", 25)

#caracterizando o dados do pet
pet1 = Pet ("toto", 5, 5.6)
pet2 = Pet ("birulinha", 4, 8.9)


print("====== Dados do dono ======")
print(f"{pessoa1.nome}, idade: {pessoa1.idade}")
print(f"{pessoa2.nome}, idade: {pessoa2.idade}")


print("====== Dados do pet ======")


print(f"Nome: {pet1.nome}, Idade: {pet1.idade} Peso: {pet1.peso}")
print(f"Nome: {pet2.nome}, Idade: {pet2.idade} Peso: {pet2.peso}")