import random
import string
import secrets

class PasswordGenerator:
    def __init__(self):
        self.lowercase = string.ascii_lowercase
        self.uppercase = string.ascii_uppercase
        self.digits = string.digits
        self.symbols = '!@#$%^&*()_+-=[]{}|;:,.<>?'

    def generate_password(self, length=12, use_upper=True, use_digits=True, use_symbols=True):
        characters = self.lowercase
        
        if use_upper:
            characters += self.uppercase
        if use_digits:
            characters += self.digits
        if use_symbols:
            characters += self.symbols
        
        if not characters:
            raise ValueError("At least one character type must be selected")
        
        password = ''.join(secrets.choice(characters) for _ in range(length))
        return password
    
    def check_strength(self, password):
        """Check password strength"""
        score = 0
        if len(password) >= 8: score += 1
        if any(c.islower() for c in password): score += 1
        if any(c.isupper() for c in password): score += 1
        if any(c.isdigit() for c in password): score += 1
        if any(c in self.symbols for c in password): score += 1
        
        if score == 5: return "Very Strong"
        if score >= 3: return "Strong"
        return "Weak"