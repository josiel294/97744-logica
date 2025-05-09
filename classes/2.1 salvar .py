import os 
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Cliente:
    marca: str 
    modelo: str
    categoria: str 
    preco: float

lista_clientes = []

QUANTIDADES_CLIENTES = 2


for i in range (QUANTIDADES_CLIENTES):
    cliente = Cliente( #instanciando um objeto 
        marca = input("Marca: "),  #adicionar virgula menos no ultimo 
        modelo = input("Modelo: "),
        categoria = input("Categoria: "), 
        preco = float(input("Preço: "))

    )
    lista_clientes.append(cliente)
    print()

print("\n= Exibindo dados clientes =")
for cliente in lista_clientes:
    print(f"Marca: {cliente.marca}")
    print(f"Modelo: {cliente.modelo}")
    print(f"Categoria: {cliente.categoria}")
    print(f"Preço: {cliente.preco}")
    print()

print("= Salvando os dados dos arquivos =")
nome_arquivo = "dados_clientes.txt"

# w -> escrita/salvar/sobrescrever
# a -> escrita/salvar/acumular

with open(nome_arquivo, "w") as arquivo:
    for cliente in lista_clientes:
        arquivo.write(f"{cliente.marca}, {cliente.modelo}, {cliente.categoria} e {cliente.preco}\n")

print("\nSalvo com sucesso!")
