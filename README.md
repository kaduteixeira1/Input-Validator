# 🔒 Validador de Senhas Seguras com Expressões Regulares

Este é um programa simples em Python que valida senhas com base em critérios de segurança, utilizando **expressões regulares**. Foi desenvolvido como parte de um trabalho acadêmico que envolve a aplicação prática de **autômatos finitos não-determinísticos com movimentos vazios (AFNe)** e **expressões regulares**.

---

## 📌 Requisitos para uma senha válida

A senha deve conter:

- ✅ Pelo menos **8 caracteres**
- ✅ Pelo menos **1 letra minúscula** (`a-z`)
- ✅ Pelo menos **1 letra maiúscula** (`A-Z`)
- ✅ Pelo menos **1 número** (`0-9`)
- ✅ Pelo menos **1 caractere especial**: `!@#$%^&*()-+`


## Exemplo de uso:
Digite a senha para validar (ou 'sair' para encerrar): MinhaSenha123!
Senha válida!

# 🧠 Expressão Regular Utilizada
```bash
^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!@#$%^&*()\-+]).{8,}$
```


