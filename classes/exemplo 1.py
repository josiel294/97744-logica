import os
os.system("clear || cls")

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


#Exemplo de uso da classe

pessoa1 = Pessoa ("Alice", 30)
pessoa2 = Pessoa ("Bob", 25)

print(f"{pessoa1.nome}, idade: {pessoa1.idade}")
print(f"{pessoa2.nome}, idade: {pessoa2.idade}")