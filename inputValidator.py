import re

def validate_password(password):
    pattern = r'^(?=.*[!@#$%^&*()\-+])(?=.*[A-Z])(?=.*\d)(?=.*[a-z]).{8,}$'
    if re.match(pattern, password):
        return "✅ Valid password!"
    else:
        return "❌ Invalid password. Requirements: 8+ characters, 1 lowercase, 1 uppercase, 1 number, 1 special character."

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    if re.match(pattern, email):
        return "✅ Valid email!"
    else:
        return "❌ Invalid email format."

def validate_phone(phone):
    pattern = r'^\+\d{1,3}\s?\(?\d{1,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{4}$'
    if re.match(pattern, phone):
        return "✅ Valid phone number!"
    else:
        return "❌ Invalid phone number. Example: +55 (11) 91234-5678"
    
def main():
    while True:
        print("\nValidation Options:")
        print("1. Validate Password")
        print("2. Validate Email")
        print("3. Validate Phone Number")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            pwd = input("Enter password: ")
            print(validate_password(pwd))
        elif choice == "2":
            email = input("Enter email: ")
            print(validate_email(email))
        elif choice == "3":
            phone = input("Enter phone number (e.g., +55 11 91234-5678): ")
            print(validate_phone(phone))
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3 or 4.")

if __name__ == "__main__":
    main()
