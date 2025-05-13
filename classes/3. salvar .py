import os
from dataclasses import dataclass
os.system("cls||clear")


@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def ler_dados_catalogo(self):
        print(f"\nNome do livro: {self.nome}")
        print(f"Nome do autor: {self.autor}")
        print(f"Categoria: {self.categoria}")
        print(f"Preço: R$ {self.preco:.2f}")


lista_livros = []

QUANTIDADES_LISTAS = 3

for i in range(QUANTIDADES_LISTAS):
    livro1 = Livro(
        nome=input("Digite o nome do livro: "),
        autor=input("Digite o nome do autor: "),
        categoria=input("Digite o nome da categoria: "),
        preco=float(input("Digite o valor do livro: "))
    )
    lista_livros.append(livro1)  # Adicionando o livro à lista

nome_arquivo = "dados_catalogo.txt"

print("= Salvando os dados dos arquivos =")

# 'w' -> escrita/salvar/sobrescrever
with open(nome_arquivo, "w") as arquivo:
    for livro in lista_livros:
        arquivo.write(f"{livro.nome}, {livro.autor}, {livro.categoria}, R$ {livro.preco:.2f}\n")

print("\nSalvo com sucesso!")

# Mostrando dados dos livros cadastrados
for livro in lista_livros:
    livro.ler_dados_catalogo()
