#!/usr/bin/python3

# Encrypt a single string

# Import Libraries

from cryptography.fernet import Fernet

# Declare Functions

def write_key():
    # Generates a key and save it into a file
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

def encrypt_file(file_content):
    encrypted_file_content = f.encrypt(file_content)
    with open ("encrypted_file.txt", "wb") as encrypted_file:
        encrypted_file.write(encrypted_file_content)
    return encrypted_file_content

def load_file():
    return open("file.txt", "rb").read()
# Main

# Generate and write a new key
write_key()

# load the previously generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))

file_content = load_file()

print("Plaintext is " + str(file_content.decode('utf-8')))

# Initialize the Fernet class
f = Fernet(key)
# Encrypt the message
encrypted = encrypt_file(file_content)

# Print how it looks
print("Ciphertext is " + encrypted.decode('utf-8'))