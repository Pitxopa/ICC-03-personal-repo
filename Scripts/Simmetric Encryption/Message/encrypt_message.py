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

def encrypt_message(message):
    encrypt_message = f.encrypt(message)
    with open ("messsage.txt", "wb") as message_file:
        message_file.write(encrypt_message)
    return encrypt_message

# Main

# Generate and write a new key
write_key()

# load the previously generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))

message = "This is a secret message".encode()
print("Plaintext is " + str(message.decode('utf-8')))

# Initialize the Fernet class
f = Fernet(key)
# Encrypt the message
encrypted = encrypt_message(message)

# Print how it looks
print("Ciphertext is " + encrypted.decode('utf-8'))