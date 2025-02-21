import os
os.system("clear")

#solocitar dados

print(""""
================= MENU =============
Código  \tPrato            \t\tValor                     
1  \t\tPicanha         \t\t300,00                      
2  \t\tCalango          \t\t15,00                      
3  \t\tPão com rato     \t\t8,00                      
4  \t\tMacaco com gripe\t\t9,00                  
5  \t\tJacare com aides\t\t25,50                      
""")



opcao = float(input("Digite o numero do seu prato: "))


#processamento
match opcao:
    case 1:
        prato = "Picanha" 
        valor = 300.00
    case 2:
        prato = "Calango"
        valor = 15.00
    case 3:
        prato = "Pão com rato"
        valor = 8.00
    case 4:
        prato = "Macaco com gripe"
        valor = 9.00
    case 5:
        prato = "Jacare com aides"
        valor = 25.50
    case _:
        reaultado = 0 
        print("prato não encontrado.")    
        print("tente com outro prato")

#exibir

print(f"Prato escolhido: {prato}")
print(f"valor: R${valor: .2f}")

