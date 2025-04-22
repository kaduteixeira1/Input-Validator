import re

def validar_senha(senha):
    padrao = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-+]).{8,}$'
    if re.match(padrao, senha):
        return "Senha válida!"
    else:
        return "Senha inválida. Requisitos: 8+ caracteres, 1 minúscula, 1 maiúscula, 1 número, 1 especial."

# Execução exemplo
while True:
    senha = input("Digite a senha para validar (ou 'sair' para encerrar): ")
    if senha.lower() == "sair":
        break
    print(validar_senha(senha))
