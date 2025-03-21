import os
os.system("cls||clear")


# Inicializa as variáveis
soma_notas = 0
contador = 0

while True:
    # Pergunta ao usuário para inserir uma nota
    nota = float(input("Digite a nota do aluno: "))
    
    # Soma a nota à variável soma_notas
    soma_notas += nota
    contador += 1  # Incrementa o contador de iterações
    
    # Pergunta ao usuário se deseja inserir mais uma nota
    mais_notas = input("Deseja inserir mais uma nota? (S/N): ").lower()
    
    # Se a resposta for "N", o programa sai do loop
    if mais_notas == "n":
        break

# Calcula a média aritmética
if contador > 0:  # Para evitar divisão por zero
    media = soma_notas / contador
    print(f"A média aritmética das notas é: {media:.2f}")
else:
    print("Nenhuma nota foi informada.")
