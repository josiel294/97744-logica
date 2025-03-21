import os
os.system ("cls || clear")

login_correto = "josiel"
senha_correta = "josiel123"

while True:
    login = input("Digite seu login: ")
    senha = input("Digite sua senha: ")
    if login == login_correto and senha == senha_correta:
        print("Login bem-sucedido!")
        break  # Sai do loop caso o login e a senha estejam corretos
    else:
        print("Login ou senha incorretos. Tente novamente.")
