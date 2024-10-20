# text - yash
# key (autometic)

import random

def generate_random_key():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shuffled_alphabet = list(alphabet)
    random.shuffle(shuffled_alphabet)
    return ''.join(shuffled_alphabet)

def monoalphabetic_encrypt():
    plain_text = input("Enter the text to encrypt: ").lower()
    key = generate_random_key()
    print(f"Generated Key: {key}")
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ""

    for char in plain_text:
        if char.isalpha():
            index = alphabet.index(char)
            encrypted_text += key[index]
        else:
            encrypted_text += char

    return encrypted_text


encrypted_text = monoalphabetic_encrypt()
print(f"Encrypted Text: {encrypted_text}")

def monoalphabetic_decrypt():
    encrypted_text = input("Enter the text to decrypt: ").lower()
    key = input("Enter the 26-letter key for decryption: ").lower()
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decrypted_text = ""

    for char in encrypted_text:
        if char.isalpha():
            index = key.index(char)
            decrypted_text += alphabet[index]
        else:
            decrypted_text += char

    return decrypted_text


decrypted_text = monoalphabetic_decrypt()
print(f"Decrypted Text: {decrypted_text}")

