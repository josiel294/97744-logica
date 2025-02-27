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
    case 2:
        parcelas = int(input("Digite a quantidade de parcelas: "))
        match parcelas:
            case "2":
                parcelass = parcelas / 2
            case "3":   
    
    case _:
        print("opcao invalida")
        
#exibir

print(f"Valor escolhido: {preco}")
print(f"Valor total do desconto: R${desconto: .2f}")
print(f"Valor total: R${valor_total: .2f}")

