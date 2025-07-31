import re

def check_strength(password):
    length = len(password) >= 8
    digit = re.search(r"\d", password)
    upper = re.search(r"[A-Z]", password)
    lower = re.search(r"[a-z]", password)
    symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)

    if all([length, digit, upper, lower, symbol]):
        return "Strong Password"
    else:
        return "Weak Password (Use uppercase, lowercase, digit & symbol)"

pwd = input("Enter password to check: ")
print(check_strength(pwd))
