import re
import getpass
from termcolor import colored

def check_password_strength(password):
    strength = 0
    feedback = []
    
    # Length Check
    if len(password) >= 12:
        strength += 2
    elif len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Upper and Lower Case Check
    if re.search("[a-z]", password) and re.search("[A-Z]", password):
        strength += 2
    else:
        feedback.append("Use both uppercase and lowercase letters.")
    
    # Numbers Check
    if re.search("[0-9]", password):
        strength += 2
    else:
        feedback.append("Include at least one number.")
    
    # Special Characters Check
    if re.search("[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 2
    else:
        feedback.append("Use special characters like @, #, $ for a stronger password.")
    
    # Common Patterns Check
    common_patterns = ["password", "1234", "qwerty", "admin"]
    if any(pattern in password.lower() for pattern in common_patterns):
        strength = 1  # Reset to weak if common pattern found
        feedback.append("Avoid common words or sequences like 'password' or '1234'.")
    
    return strength, feedback

def display_strength(strength):
    if strength >= 7:
        return colored("STRONG", "green")
    elif strength >= 4:
        return colored("MEDIUM", "yellow")
    else:
        return colored("WEAK", "red")

if __name__ == "__main__":
    password = getpass.getpass("Enter your password: ")
    strength, feedback = check_password_strength(password)
    print(f"Password Strength: {display_strength(strength)}")
    
    if feedback:
        print("\nSuggestions to improve your password:")
        for tip in feedback:
            print(f"- {tip}")
