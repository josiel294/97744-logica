import os
os.system("clear")

#solocitar dados
mes_do_ano = str(input("Digite o primeiro numero: "))


#processamento

match mes_do_ano:
    case "1":
        mes_do_ano = "janeiro"
    case "2":
        mes = "fevereiro"
    case "3":
        mes = "março" 
    case "4":
        mes = "abril"
    case "5":
        mes = "maio"
    case "6":
        mes = "junho"
    case "7":
        mes = "julho"
    case "8":
        mes = "agosto"
    case "9":
        mes = "setembro"
    case "10":
        mes = "outubro"
    case "11":
        mes = "novembro"
    case "12":
        mes = "dezembro"
    case _:
        mes = "MES NAO ENCONTRADO, TENTE NOVAMENTE."


#exibir

print(f"MES ESCOLHIDO: {mes_do_ano}")
print(f"NOME DO MES: {mes}")

