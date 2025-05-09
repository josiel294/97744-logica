import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Livro:
    nome_livro:str
    livro_ano: int

@dataclass
class Autor:
    nome: str
    livro: Livro

    def exibir_detelhes(self):
        print(f"\nNome do Autor: {self.nome}")
        print(f"\nNome do livro: {self.livro.nome_livro}")
        print(f"\nAno do livro: {self.livro.livro_ano}")

nome_livro1 = Livro ("Mundão de ilusão", 2023)
nome1 = Autor ("Mundão de ilusão", nome_livro1)
nome1.exibir_detelhes()