def vigenere_encrypt(plaintext, key):
    key = (key * (len(plaintext) // len(key))) + key[:len(plaintext) % len(key)]
    ciphertext = []
    for p, k in zip(plaintext, key):
        if p.isalpha():
            shift = ord(k.upper()) - ord('A')
            encrypted_char = chr((ord(p.upper()) - ord('A') + shift) % 26 + ord('A'))
            ciphertext.append(encrypted_char)
        else:
            ciphertext.append(p)
    return ''.join(ciphertext)
plaintext = input("Enter the plaintext: ")
key = input("Enter the key: ")
ciphertext = vigenere_encrypt(plaintext, key)
print(f"Encrypted text: {ciphertext}")






#Decryption
def vigenere_decrypt(ciphertext, key):
    key = (key * (len(ciphertext) // len(key))) + key[:len(ciphertext) % len(key)]
    plaintext = []
    for c, k in zip(ciphertext, key):
        if c.isalpha():
            shift = ord(k.upper()) - ord('A')
            decrypted_char = chr((ord(c.upper()) - ord('A') - shift + 26) % 26 + ord('A'))
            plaintext.append(decrypted_char)
        else:
            plaintext.append(c)
    return ''.join(plaintext)
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")
plaintext = vigenere_decrypt(ciphertext, key)
print(f"Decrypted text: {plaintext}")
