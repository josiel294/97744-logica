import os
os.system("cls||clear")


def calcular (peso, altura):
    calculo_indice = peso / (altura * altura) 
    return calculo_indice

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
    
indice_total = calcular(peso, altura)

if indice_total <18:
    print("Abaixo do peso\nConsulte um nutricionista")
elif indice_total > 18.5:
    print("Peso normal\nMantenha hábitos saudáveis!")
elif indice_total >= 25:
    print("Sobrepeso\nConsidere uma dieta balanceada e atividade física")
elif indice_total >= 30:
    print("Obesidade grau 1\nProcure uma orientação de um profissional de saúde")
elif indice_total >= 35:
    print("Obesidade grau 2\nConsulte um médico para avaliação e orientação")
elif indice_total >=40:
    print("Obesidade grau 3\nBusque assistência médica imediatamente")
else:
    print("Nenhum valor encontrado tente novamente")

print(f"Peso: {peso}")
print(f"Altura: {altura}")