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

lista_autor = []

for i in range (3):
    print()
    autor1 = Autor(
        nome = input("Digite o nome do autor: "),
        livro = Livro(
            nome_livro = input("Digite o nome do livro: "),
            livro_ano = int(input("Digite o ano da data de publicação do livro: "))
    )
)



autor1.exibir_detelhes()


