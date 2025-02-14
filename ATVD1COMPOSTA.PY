import os
os.system("clear")

#solocitar dados
numero_um = int(input("Digite o primeiro numero: "))
numero_dois = int(input("Digite o segundo numero: "))
print()
media: int
soma: int
produto: int

#processamento


media = (numero_um + numero_dois) / 2

soma = numero_um + numero_dois

produto = numero_um * numero_dois


maior_numero = max(numero_um, numero_dois)
menor_numero = min(numero_um, numero_dois)


print(f"NUMERO UM: ", {numero_um})
print()
print(f"NUMERO DOIS: ", {numero_dois})
print()
print(f"NUMERO DA MEDIA: ", {media})
print()
print(f"NUMERO DA SOMA: ", {soma})
print()
print(f"NUMERO DO PRODUTO: ", {produto})

if numero_um == numero_dois:
    print(f"Os números são iguais")
else:
    print(f"Maior_numero: {maior_numero}")
    print(f"Menor_numero: {menor_numero}")


