import os
os.system ("cls || clear")

login_correto = "josiel"
senha_correta = "josiel123"

tentativas = 0
max_tentativas = 3

while tentativas < max_tentativas:
     login = input("Digite seu login: ")
     senha = input("Digite sua senha: ")
     if login == login_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break  # Sai do loop caso o login e a senha estejam corretos
     else:
        tentativas += 1
        print(f"Login ou senha incorretos. Tentativas restantes: {max_tentativas - tentativas}")

if tentativas == max_tentativas:
    print("Número de tentativas excedido. Programa finalizado.")