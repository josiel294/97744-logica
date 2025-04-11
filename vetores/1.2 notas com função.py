import os
os.system("cls||clear")

def calcular_media_e_resultado(quantidade_notas = 4):
    notas = []
    for i in range(quantidade_notas):
        nota = float(input("Digite sua nota: "))
        notas.append(nota)
        
    media = sum(notas) / quantidade_notas

    if media >7:
        resultado = "Aprovado"
    elif media > 5:
        resultado ="Recuperação"
    else:
        resultado = "Reprovado"
        
    print("\nNotas inseridas")

    for nota in notas:
        print(f"Notas: {nota}")

    print(f"{media: .2f}")
    print(f"{resultado}")

    return media, resultado, notas


media, resultado, notas = calcular_media_e_resultado()

