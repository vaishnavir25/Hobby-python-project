from cryptography.fernet import Fernet

# Step 1: Generate a key and save it to a file
def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

# Step 2: Load the key from the file
def load_key():
    with open("secret.key", "rb") as key_file:
        return key_file.read()

# Step 3: Encrypt a file
def encrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    # Read the file to encrypt
    with open(file_name, "rb") as file:
        data = file.read()

    # Encrypt the data
    encrypted_data = fernet.encrypt(data)

    # Save the encrypted data back to the file
    with open(file_name, "wb") as file:
        file.write(encrypted_data)
    print(f"{file_name} has been encrypted!")

# Step 4: Decrypt a file
def decrypt_file(file_name):
    key = load_key()
    fernet = Fernet(key)

    # Read the encrypted file
    with open(file_name, "rb") as file:
        encrypted_data = file.read()

    # Decrypt the data
    decrypted_data = fernet.decrypt(encrypted_data)

    # Save the decrypted data back to the file
    with open(file_name, "wb") as file:
        file.write(decrypted_data)
    print(f"{file_name} has been decrypted!")

# Example usage
if __name__ == "__main__":
    generate_key()  # Run this only once to generate a key

    file_name = "example.txt"
    # Create a sample file to encrypt
    with open(file_name, "w") as file:
        file.write("This is a secret message.")

    encrypt_file(file_name)  # Encrypt the file
    decrypt_file(file_name)  # Decrypt the file
