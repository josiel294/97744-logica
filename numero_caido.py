import os
os.system("clear")

#solocitar dados
dia_da_semana = str(input("Digite o primeiro numero: "))


#processamento

match dia_da_semana:
    case "1":
        dia_semana = "DOMINGO"
        dia_util = "FINAL DE SEMANA"
    case "2":
        dia_semana = "SEGUNDA"
        dia_util = "útil"
    case "3":
        dia_semana = "TERÇA"
        dia_util = "útil"
    case "4":
        dia_semana = "QUARTA"
        dia_util = "útil"
    case "5":
        dia_semana = "QUINTA" 
        dia_util = "útil"
    case "6":
        dia_semana = "SEXTA"
        dia_util = "útil"
    case "7":
        dia_semana = "SABADO"
        dia_util = "FINAL DE SEMANA"
    case _:
        resultado = 0 
        print("prato não encontrado.")    
        print("tente com outro prato")


#exibir

print(f"DIA DA SEMANA ESCOLHIDO: {dia_da_semana}")
print(f"DIA DA SEMANA: {dia_semana}")
print(f"DIA É ÚTIL?: {dia_util}")
