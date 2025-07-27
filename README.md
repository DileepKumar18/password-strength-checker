# 🔐 Password Strength Checker

A simple Python script to check the strength of a password based on common security best practices.

## ✅ Features

- Checks for length, uppercase, lowercase, digits, special characters
- Flags common weak passwords
- Detects repeated patterns
- Provides feedback and suggestions

## 📦 Requirements

- Python 3.x

## 🚀 How to Run

```bash
python password_checker.py
```

## 🛡️ Password Rules

1. Minimum 8 characters
2. At least one uppercase letter
3. At least one lowercase letter
4. At least one number
5. At least one special character
6. Not a common password
7. No repeated characters (e.g., "aaa", "111")

## 🧪 Example Output

```
Enter your password: Admin123

Password Strength Score: 4/5
⚠️ Weak password. Suggestions:
 - Include at least one special character.
```

