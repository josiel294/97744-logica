import os 
os.system ("cls||clear")



def calcular_media(lista):
    media = sum (lista) / len(lista)
    return media
# sum (lista) irá somar os valores na lista.
#  len (lista) irá mostrar a quantidade de valores na lista



lista_notas = []
QUANTIDADE_NOTAS = 2 

for i in range(QUANTIDADE_NOTAS):
    nota = float(input(f"Digite a {i+1}° nota: "))
    lista_notas.append (nota)
# Chamando a função para calcular a média. 
# Enviando a lista de notas como parâmetro.
# Inserindo na variável 'media' o cáculo retornado pela função.
media = calcular_media(lista_notas)

print(f"\nMédia: {media}")