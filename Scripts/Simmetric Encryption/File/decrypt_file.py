#!/usr/bin/python3

from cryptography.fernet import Fernet

# Declare Functions

def load_key():
    return open("key.key", "rb").read()

def decrypt_file(file_content):
    decrypted_file_content = f.decrypt(file_content)
    with open("decrypted_file.txt", "wb") as decrypted_file:
        decrypted_file.write(decrypted_file_content)
    return decrypted_file_content

def load_file():
    return open("encrypted_file.txt", "rb").read()

# Main

key = load_key()
print("Key is " + str(key.decode('utf-8')))

file_content = load_file()

# Initialize the Fernet class
f = Fernet(key)

decrypt = decrypt_file(file_content)

print("Decrypted text is " + decrypt.decode('utf-8'))