import os
os.system("clear")

#solocitar dados
quantidade_maca = int(input("Digite o numero de maçãs que deseja comprar: "))

#processamento
if quantidade_maca < 12:
    preco_de_maca = 1.30
else:
    preco_de_maca = 1.0




valor_total = quantidade_maca * preco_de_maca



#exibir dados
print(f"Valor total da compra:  {valor_total: .2f}")