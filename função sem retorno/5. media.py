import os
os.system("cls||clear")
import time

def verificar_uniade1 (media1):
    if media1 > 7: 
        print("Aluno Aprovado!")
    else:
        print("Aluno Reprovado!")


def verificar_uniade2 (media2):
    if media2 > 7: 
        print("Aluno Aprovado!")
    else:
        print("Aluno Reprovado!") 

media1 = float(input("Digite sua nota da primeira unidade: "))    
media2 = float(input("Digite sua nota da segunda unidade: "))
print("Verificando resultados...")
time.sleep(2)
verificar_uniade1(media1)
verificar_uniade2(media2)
