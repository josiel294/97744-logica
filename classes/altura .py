import os
from dataclasses import dataclass
import time
os.system("cls || clear")

@dataclass
class Pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

pessoa1 = Pessoa(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura: "))
) 

print()

pessoa2 = Pessoa(
    nome = input("Digite seu nome: "),
    idade = int(input("Digite sua idade: ")),
    peso = float(input("Digite seu peso: ")),
    altura = float(input("Digite sua altura : "))
)

print()

time.sleep(3)
print("=== DADOS ===")

print(f"Nome: {pessoa1.nome}, Idade: {pessoa1.idade}, Peso: {pessoa1.peso}, Altura: {pessoa1.altura}")
print()
print(f"Nome: {pessoa2.nome}, Idade: {pessoa2.idade}, Peso: {pessoa2.peso}, Altura: {pessoa2.altura}")

print("Obrigado pela atenção!")