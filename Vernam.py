def vernam_cipher(plaintext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_index = 0
    ciphertext = ''

    for char in plaintext:
        if char.isalpha():
            shift = alphabet.index(key[key_index % len(key)].lower())
            if char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            else:
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            key_index += 1
        elif char.isnumeric():
            ciphertext += char
        else:
            ciphertext += char

    return ciphertext

plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")

ciphertext = vernam_cipher(plaintext, key)
print("Ciphertext:", ciphertext)


def vernam_decipher(ciphertext, key):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_index = 0
    plaintext = ''

    for char in ciphertext:
        if char.isalpha():
            shift = alphabet.index(key[key_index % len(key)].lower())
            if char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            key_index += 1
        elif char.isnumeric():
            plaintext += char
        else:
            plaintext += char

    return plaintext

# User input for decryption
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

decrypted_text = vernam_decipher(ciphertext, key)
print("Decrypted Text:", decrypted_text)
