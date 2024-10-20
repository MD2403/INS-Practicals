# TEXT- yash
# key (autometic)

import random

def generate_key(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(length))

def one_time_pad_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("The length of the key must match the length of the plaintext")
    
    ciphertext = []
    for p, k in zip(plaintext, key):
        c = chr(((ord(p) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A'))
        ciphertext.append(c)
    
    return ''.join(ciphertext)


plaintext = input("Enter the plaintext (uppercase letters only): ").upper()
key = generate_key(len(plaintext))
ciphertext = one_time_pad_encrypt(plaintext, key)
print(f"Generated Key: {key}")
print(f"Encrypted Text: {ciphertext}")

def one_time_pad_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("The length of the key must match the length of the ciphertext")
    
    plaintext = []
    for c, k in zip(ciphertext, key):
        p = chr(((ord(c) - ord('A')) - (ord(k) - ord('A')) + 26) % 26 + ord('A'))
        plaintext.append(p)
    
    return ''.join(plaintext)

ciphertext = input("Enter the ciphertext (uppercase letters only): ").upper()
key = input("Enter the key (uppercase letters only): ").upper()
plaintext = one_time_pad_decrypt(ciphertext, key)
print(f"Decrypted Text: {plaintext}")
