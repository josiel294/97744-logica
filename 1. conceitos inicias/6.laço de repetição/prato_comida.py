import os
os.system("cls||clear")

#solocitar dados

print(""""
================= MENU =============
Código  \tPrato            \t\tValor                     
1  \t\tPicanha         \t\t25,00                      
2  \t\tLasanha          \t\t20,00                      
3  \t\tStrogonoff      \t\t18,00                      
4  \t\tbife acebolado  \t\t15,00                  
5  \t\tPão com ovo     \t\t5,00                      
""")

pedidos = []
valor_total = 0

while True:
    escolha = int(input("escolha o prato desejado (1-6): "))
    if escolha ==1:
        pedidos.append("Prato 1 - R$ 25,00")
        valor_total += 25.00
    elif escolha ==2:
        pedidos.append("Prato 2 - R$ 20,00")
        valor_total += 20.00
    elif escolha ==3:
        pedidos.append("Prato 3 - R$ 18,00")
        valor_total += 18.00
    elif escolha ==4:
        pedidos.append("Prato 4 - R$ 15,00")
        valor_total += 15.00
    elif escolha ==5:
        pedidos.append("Prato 5 - R$ 5,00")
        valor_total += 5.00
        break
    else:
        print("opção invalida, tente novamente")
        continue

    continuar = input("\nDeseja escolher outro prato? (s/n): ").lower()
    if continuar != 's':
        break  # Sai do loop se o usuário não quiser continuar

print("Pedido finalizado!")

for prato in pedidos:
    print(prato)

print(f"Valor total: {valor_total: .2f}")



        


