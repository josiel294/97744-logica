import os
os.system("clear")

#solocitar dados
preco = int(input("Digite o valor do pagamento: "))


print(""""
================= FORMA DE PAGAMENTO =============
Código  \tPrato                      
1  \t\tÁ vista ou pix                   
2  \t\tÁ prazo                             
""")

forma_de_pagamento = int(input("forma de pagamento: "))


#processamento
match forma_de_pagamento:
    case 1:
        desconto = (preco * 0.10) 
        valor_total = preco - desconto
        print(f"Valor total do produto: {preco}")
        print(f"Valor total do pagamento: {valor_total}")
    case 2:
        parcelas = int(input("Digite a quantidade de parcelas: "))
        if parcelas >= 1 and parcelas <= 6:
            valor_da_parcela = preco / parcelas
            print(f"\nValor do produto: R$ {preco}")
            print(f"Forma de pagamento: à prazo")
            print(f"Quantidade de parcelas: {parcelas}")
            print(f"Valor por parcela: R$ {valor_da_parcela:.2f}")
            print(f"Total à prazo: R$ {valor_da_parcela}")
        else:
            print("opcao invalida.")
    case _:
         print("opcao invalida")          
    


#exibir


