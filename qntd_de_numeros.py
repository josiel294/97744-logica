import os
os.system("cls||clear")


# Inicializa as variáveis para contar pares, ímpares, soma dos pares e soma geral
quantidade_pares = 0
quantidade_impares = 0
soma_pares = 0
soma_geral = 0
contador = 0

# Laço de leitura até o número 0 ser informado
while True:
    numero = int(input("Digite um número inteiro positivo (0 para encerrar): "))
    
    # Se o número for 0, o programa encerra
    if numero == 0:
        break
    
    # Verifica se o número é par ou ímpar e atualiza as variáveis
    if numero % 2 == 0:
        quantidade_pares += 1
        soma_pares += numero
    else:
        quantidade_impares += 1
    
    # Soma o número à soma geral
    soma_geral += numero
    contador += 1

# Cálculos das médias
media_pares = soma_pares / quantidade_pares if quantidade_pares > 0 else 0
media_geral = soma_geral / contador if contador > 0 else 0

# Exibe os resultados
print(f"Quantidade de números pares: {quantidade_pares}")
print(f"Quantidade de números ímpares: {quantidade_impares}")
print(f"Média dos números pares: {media_pares:.2f}")
print(f"Média geral dos números lidos: {media_geral:.2f}")
