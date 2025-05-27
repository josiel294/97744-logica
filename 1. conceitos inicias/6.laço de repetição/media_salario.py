import os
os.system ("cls||clear")

import os

# Listas para armazenar os dados coletados
idades = []
sexos = []
salarios = []

# Laço principal
while True:
    # Exibe o menu
    print("Menu:")
    print("1 - Adicionar pessoa")
    print("2 - Exibir resultados")
    print("3 - Sair")
    
    # Solicita a opção ao usuário
    opcao = input("Escolha uma opção (1/2/3): ")
    
    # Se escolher adicionar pessoa (opção 1)
    if opcao == '1':
        idade = int(input("Digite a idade da pessoa: "))
        sexo = input("Digite o sexo da pessoa (M/F): ").upper()
        salario = float(input("Digite o salário da pessoa: "))
        
        # Armazena os dados nas listas
        idades.append(idade)
        sexos.append(sexo)
        salarios.append(salario)
        
        # Limpa o terminal
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Se escolher exibir resultados (opção 2)
    elif opcao == '2':
        if not idades:
            print("Nenhum dado foi inserido ainda!")
        else:
            # a) Média de salário do grupo
            media_salario = sum(salarios) / len(salarios)
            
            # b) Maior e menor idade do grupo
            maior_idade = max(idades)
            menor_idade = min(idades)
            
            # c) Quantidade de mulheres com salário a partir de 5000
            mulheres_acima_5000 = sum(1 for i, s in enumerate(sexos) if s == 'F' and salarios[i] >= 5000)
            
            # Exibe os resultados
            print(f"Média de salário do grupo: R${media_salario:.2f}")
            print(f"Maior idade do grupo: {maior_idade} anos")
            print(f"Menor idade do grupo: {menor_idade} anos")
            print(f"Quantidade de mulheres com salário a partir de 5.000,00: {mulheres_acima_5000}")
    
    # Se escolher sair (opção 3)
    elif opcao == '3':
        print("Saindo do programa...")
        break
    
    # Caso a opção seja inválida
    else:
        print("Opção inválida! Tente novamente.")
