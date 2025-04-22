import re

def validate_password(password):
    pattern = r'^(?=.*[!@#$%^&*()\-+])(?=.*[A-Z])(?=.*\d)(?=.*[a-z]).{8,}$'
    if re.match(pattern, password):
        return "Valid password!"
    else:
        return "Invalid password. Requirements: 8+ characters, 1 lowercase, 1 uppercase, 1 number, 1 special character."

while True:
    password = input("Enter the password to validate (or type 'exit' to quit): ")
    if password.lower() == "exit":
        break
    print(validate_password(password))
