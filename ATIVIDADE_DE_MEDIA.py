import os
os.system ("clear")


#Solicitar dados
primeira_unidade = float(input("Digite a nota da sua primeira unidade: "))
segunda_unidade = float(input("Digite a nota da sua segunda unidade: "))
terceira_unidade = float(input("Digite a nota da sua terceira unidade: "))
media: float


media = (primeira_unidade + segunda_unidade + terceira_unidade)/3


#exibir dados
print(f"Nota da primeira unidade: ", primeira_unidade)
print() 
print(f"Nota da segunda unidade: ", segunda_unidade)
print()
print(f"Nota da terceira unidade: ", terceira_unidade)
print()
print(f"Sua media final: ", media)

if media < 7:
    print("Reprovado!") 
else :
    print("Aprovado!")

