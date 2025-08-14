import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_strength(password):
    strength = 0
    if any(c.islower() for c in password):
        strength += 1
    if any(c.isupper() for c in password):
        strength += 1
    if any(c.isdigit() for c in password):
        strength += 1
    if any(c in string.punctuation for c in password):
        strength += 1

    if strength == 4 and len(password) >= 12:
        return "Very Strong 💪"
    elif strength >= 3:
        return "Strong 👍"
    elif strength == 2:
        return "Moderate 😐"
    else:
        return "Weak ❌"

if __name__ == "__main__":
    length = int(input("Enter password length: "))
    pwd = generate_password(length)
    print(f"🔑 Your password: {pwd}")
    print(f"📊 Strength: {password_strength(pwd)}")
