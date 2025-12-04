#!/usr/bin/python3

# Encrypt a single string

# Import Libraries

from cryptography.fernet import Fernet

# Declare Functions



def load_key():
    # Loads the key from the current directory named `key.key`
    return open("key.key", "rb").read()

def decrypt_message(message):
    decrypt_message = f.decrypt(message)
    with open ("decrypt.txt", "wb") as message_file:
        message_file.write(decrypt_message)
    return decrypt_message

def load_message():
    return open("messsage.txt", "rb").read()

# Main


# load the previously generated key
key = load_key()
print("Key is " + str(key.decode('utf-8')))



# Initialize the Fernet class
f = Fernet(key)
# Encrypt the message
message = load_message()
print("Ciphertext is " + str(message.decode('utf-8')))
decrypted = decrypt_message(message)

# Print how it looks
print("Plaintext is " + decrypted.decode('utf-8'))