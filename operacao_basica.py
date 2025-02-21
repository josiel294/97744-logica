import os
os.system("clear")

#solocitar dados
numero_um = int(input("Digite o primeiro numero: "))
operacao = str(input("Digite a operação que você deseja: "))
numero_dois = int(input("Digite o segundo numero: "))
print()

#processamento

match operacao:
    case "/":
        resultado = numero_um / numero_dois
    case "+":
        resultado = numero_um + numero_dois
    case "*":
        resultado = numero_um * numero_dois
    case "-":
        resultado = numero_um - numero_dois
    case _:
        reaultado = 0 
        print("opção invalida.")    
        print("tente com outra operação")

#exibir

print(f"primeiro numero digitado: {numero_um}")
print(f"segundo numero digitado: {numero_dois}")
print(f"resultado: {resultado} ")