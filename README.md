# 🔎 Validador de Entradas com Expressões Regulares

Este é um programa simples em Python que valida diferentes tipos de entrada do usuário utilizando **expressões regulares**. Ele foi desenvolvido como parte de um trabalho acadêmico sobre **autômatos finitos não-determinísticos com movimentos vazios (AFNe)** e **expressões regulares**.

## 🧩 Funcionalidades

O programa valida os seguintes campos:

1. 🔒 **Senha segura**
2. 📧 **Endereço de e-mail**
3. 📱 **Número de telefone (com ou sem código internacional)**

## ▶️ Exemplo de uso

Validation Options:
1. Validate Password
2. Validate Email
3. Validate Phone Number
4. Exit

Choose an option (1-4): 1  
Enter password: MinhaSenha123!  
✅ Valid password!

## 🧠 Expressões Regulares Utilizadas

### 1. Senha
^(?=.[a-z])(?=.[A-Z])(?=.\d)(?=.[!@#$%^&*()-+]).{8,}$

| Parte                         | Significado                                |
|------------------------------|--------------------------------------------|
| `^` e `$`                    | Início e fim da string                     |
| `(?=.*[a-z])`                | Pelo menos uma letra minúscula             |
| `(?=.*[A-Z])`                | Pelo menos uma letra maiúscula             |
| `(?=.*\d)`                   | Pelo menos um número                       |
| `(?=.*[!@#$%^&*()\-+])`      | Pelo menos um caractere especial           |
| `.{8,}`                      | Pelo menos 8 caracteres no total           |

### 2. E-mail
^[\w.-]+@[\w.-]+.\w{2,}$

| Parte             | Significado                                                |
|------------------|------------------------------------------------------------|
| `^` e `$`         | Início e fim da string                                     |
| `[\w\.-]+`        | Parte local do e-mail (letras, números, `.` ou `-`)       |
| `@`               | Separador obrigatório entre usuário e domínio             |
| `[\w\.-]+`        | Nome do domínio (ex: gmail, yahoo)                        |
| `\.`              | Ponto separando o domínio do TLD (ex: `.com`)             |
| `\w{2,}`          | TLD com pelo menos 2 caracteres (ex: com, edu, org)       |


### 3. Telefone
^+?\d{1,3}\s?\d1,4?[\s.-]?\d{3,4}[\s.-]?\d{4}$

| Parte              | Significado                                                                |
|--------------------|----------------------------------------------------------------------------|
| `^` e `$`          | Início e fim da string                                                     |
| `\+?`              | Símbolo `+` opcional (para código internacional)                           |
| `\d{1,3}`          | DDI com 1 a 3 dígitos (ex: 55, 1, 351)                                     |
| `\s?`              | Espaço opcional entre o DDI e o DDD                                        |
| `\(?\d{1,4}\)?`    | DDD com ou sem parênteses, de 1 a 4 dígitos                                |
| `[\s.-]?`          | Separador opcional (espaço, ponto ou hífen)                                |
| `\d{3,4}`          | Primeira parte do número (geralmente prefixo de celular ou telefone fixo) |
| `[\s.-]?`          | Separador opcional                                                         |
| `\d{4}`            | Últimos 4 dígitos do número  

## ⚙️ Tecnologias

- Python 3
- Módulo `re` para expressões regulares

## 📚 Teoria Aplicada

Cada uma das expressões regulares representa uma linguagem reconhecível por um **AFNe (Autômato Finito Não-Determinístico com movimentos vazios)**. A validação simula esse comportamento ao verificar se a entrada pertence à linguagem definida pela expressão.
