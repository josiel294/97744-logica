import os
os.system("cls||clear")


def calcular(media1, media2, media3):
    return (media1 + media2 + media3) / 3
    


media1 = float(input("Digite a sua nota da primeira unidade: "))
media2 = float(input("Digite a sua nota da segunda unidade: "))
media3 = float(input("Digite a sua nota da terceira unidade: "))


media_total = calcular(media1, media2, media3)
print(f"Valor da media total: {media_total: .2f}")

