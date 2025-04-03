import os
os.system("cls||clear")

# Menu do cardápio
print("\n--- Cardápio do Restaurante ---")
print("1. Prato 1 - R$ 25,00")
print("2. Prato 2 - R$ 30,00")
print("3. Prato 3 - R$ 20,00")
print("4. Prato 4 - R$ 40,00")
print("5. Prato 5 - R$ 15,00")
print("6. Sair")

# Variáveis para armazenar os pedidos e o total
pedidos = []
valor_total = 0

# Loop principal
while True:
    escolha = int(input("\nEscolha o prato desejado (1-6): "))

    # Adiciona o prato escolhido ao pedido
    if escolha == 1:
        pedidos.append("Prato 1 - R$ 25,00")
        valor_total += 25.00
    elif escolha == 2:
        pedidos.append("Prato 2 - R$ 30,00")
        valor_total += 30.00
    elif escolha == 3:
        pedidos.append("Prato 3 - R$ 20,00")
        valor_total += 20.00
    elif escolha == 4:
        pedidos.append("Prato 4 - R$ 40,00")
        valor_total += 40.00
    elif escolha == 5:
        pedidos.append("Prato 5 - R$ 15,00")
        valor_total += 15.00
    elif escolha == 6:
        break  # Sai do loop se o usuário escolher "Sair"
    else:
        print("Opção inválida. Tente novamente.")
        continue  # Continua o loop se a opção for inválida

    continuar = input("\nDeseja escolher outro prato? (s/n): ").lower()
    if continuar != 's':
        break  # Sai do loop se o usuário não quiser continuar

# Exibe o resumo do pedido
print("\n--- Pedido Finalizado ---")
for prato in pedidos:
    print(prato)

print(f"\nValor total: R$ {valor_total:.2f}")

# Pergunta sobre a gorjeta
gorjeta = input("\nDeseja pagar uma gorjeta de 10% para o garçom? (s/n): ").lower()

if gorjeta == 's':
    valor_gorjeta = valor_total * 0.10
    valor_total_com_gorjeta = valor_total + valor_gorjeta
    print(f"Gorjeta de 10%: R$ {valor_gorjeta:.2f}")
    print(f"Total a pagar: R$ {valor_total_com_gorjeta:.2f}")
else:
    print(f"Total a pagar: R$ {valor_total:.2f}")
