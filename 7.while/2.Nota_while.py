import os 
os.system ("cls || clear")

soma = 0

for i in range(2):
    while True:
            nota = int(input(f"Digite o {i+ 1}º nota: ")) 
            if nota <0 or nota >10:
                  print("Nota errada \nDigite sua nota novamente.\n")
            else:
                  soma += nota
                  break  
                  
                   
media = soma / 2
        



    
print(f"Media total: {media}")