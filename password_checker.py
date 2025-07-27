import re

def check_password_strength(password):
    strength = 0
    suggestions = []

    # Rule 1: Length
    if len(password) >= 8:
        strength += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Rule 2: Uppercase letter
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        suggestions.append("Include at least one uppercase letter.")

    # Rule 3: Lowercase letter
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        suggestions.append("Include at least one lowercase letter.")

    # Rule 4: Digit
    if re.search(r"\d", password):
        strength += 1
    else:
        suggestions.append("Include at least one number.")

    # Rule 5: Special character
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        suggestions.append("Include at least one special character.")

    # Rule 6: Avoid common passwords
    common = ["password", "123456", "admin", "qwerty"]
    if any(word in password.lower() for word in common):
        suggestions.append("Avoid using common passwords like 'password', '123456', etc.")

    # Rule 7: Repeated patterns
    if re.search(r"(.)\1{2,}", password):
        suggestions.append("Avoid repeated characters or patterns.")

    return strength, suggestions

def main():
    pwd = input("Enter your password: ")
    score, advice = check_password_strength(pwd)

    print(f"\nPassword Strength Score: {score}/5")
    if score == 5:
        print("✅ Strong password!")
    else:
        print("⚠️ Weak password. Suggestions:")
        for s in advice:
            print(f" - {s}")

if __name__ == "__main__":
    main()
