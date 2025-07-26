import random
import string

def generate_password(length, use_symbols=True, use_uppercase=True):
    characters = string.ascii_lowercase + string.digits
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_symbols:
        characters += string.punctuation

    password = ''.join(random.choices(characters, k=length))
    return password

def password_generator():
    print("🔐 Advanced Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_symbols, use_uppercase)
        print("Your generated password is:", password)
    except ValueError:
        print("❌ Please enter a valid number.")

password_generator()
