import random
import string

def generate_password(length):
    """Generate a random password with the given length."""
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    characters = letters + digits + symbols
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = generate_password(12)
print(password)