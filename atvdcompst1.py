import os
os.system("clear")

#solocitar dados
numero_um = int(input("Digite o primeiro numero: "))
numero_dois = int(input("Digite o segundo numero: "))

media: float
soma: float
produto: float

#processamento

media = (numero_um + numero_dois) / 2

soma = numero_um + numero_dois

produto = numero_um * numero_dois


maior_numero = max(numero_um, numero_dois)
menor_numero = min(numero_um, numero_dois)

print(f"NUMERO UM: ", {numero_um})
print(f"NUMERO DOIS: ", {numero_dois})
print(f"NUMERO DA MEDIA: ", {media})
print(f"NUMERO DA SOMA: ", {soma})
print(f"NUMERO DA SOMA: ", {produto})
print(f"MENOR NUMERO: ", {menor_numero})
print(f"MAIOR NUMERO: ", {maior_numero})


