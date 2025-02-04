import string

def check_password_strength(password):
    length = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([has_lower, has_upper, has_digit, has_special])

    if length >= 12 and score == 4:
        return "Very Strong"
    elif length >= 10 and score >= 3:
        return "Strong"
    elif length >= 8 and score >= 2:
        return "Moderate"
    else:
        return "Weak"

def main():
    password = input("Enter a password to check its strength: ")
    strength = check_password_strength(password)
    print(f"Password Strength: {strength}")

if __name__ == "__main__":
    main()
