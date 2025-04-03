import os
os.system("cls||clear")
import time
contador = 0
soma_salario = 0
maior_salario = 0
menor_salario = 9999
mulheres5k = 0
while True:
    print("1. Adicionar pessoa")
    print("2. Sair e exibit resultados")

    opcao = int(input("Dígite a opção (1/2): "))
    match opcao:
        case 1:
            filhos = int(input("Digite quantos filhos têm: "))
            salario = float(input("Digite o valor do seu salario: "))
            contador += 1
            soma_salario += salario
            #maior_idade = idade if idade> maior_idade else maior-iadae
            if idade > maior_idade:
                maior_idade = idade
            if idade < menor_idade:
                menor_idade = idade
            if salario >:
                mulheres5k += 1 
            os.system("cls||clear")
        case 2:
            if contador >0:
                media_salario_grupo = soma_salario / contador
                print("\n= Exibindo resultados=")
                print(f"Média de salario do grupo: {media_salario_grupo}")
                print(f"Maior idade do grupo: {maior_idade}")
                print(f"Menor idade do grupo: {menor_idade}")
                print(f"Mulheres com apartir de 5mil de salario do grupo: {mulheres5k}")
                time.sleep(3)
                os.system("cls||clear")
            break

        case _:
            print("\nOpção inválida.")
            time.sleep(3)
            os.system("cls||clear")
    