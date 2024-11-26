import random
import string

# Function to generate a strong password
def generate_password(length, include_uppercase, include_digits, include_special):
    # Start with lowercase letters
    characters = string.ascii_lowercase

    # Add other character types based on user preference
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_digits:
        characters += string.digits
    if include_special:
        characters += string.punctuation

    # Generate the password by randomly choosing from the character set
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Example usage
if __name__ == "__main__":
    print("Welcome to the Password Generator!")
    
    # Get user input
    length = int(input("Enter the desired password length: "))
    include_uppercase = input("Include uppercase letters? (yes/no): ").lower() == "yes"
    include_digits = input("Include numbers? (yes/no): ").lower() == "yes"
    include_special = input("Include special characters? (yes/no): ").lower() == "yes"

    # Generate and display the password
    password = generate_password(length, include_uppercase, include_digits, include_special)
    print(f"Your generated password is: {password}")
