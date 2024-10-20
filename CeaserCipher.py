# pra 1

# text - yash
# key - 4

def caesar_encrypt():
    plain_text = input("Enter the text to encrypt: ")
    shift = int(input("Enter the shift value: "))
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            encrypted_char = chr((ord(char) - base + shift_amount) % 26 + base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

encrypted_text = caesar_encrypt()
print(f"Encrypted Text: {encrypted_text}")


def caesar_decrypt():
    encrypted_text = input("Enter the text to decrypt: ")
    shift = int(input("Enter the shift value: "))
    decrypted_text = ""
    for char in encrypted_text:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
            decrypted_char = chr((ord(char) - base - shift_amount) % 26 + base)
            decrypted_text += decrypted_char
        else:
            decrypted_text += char
    return decrypted_text


decrypted_text = caesar_decrypt()
print(f"Decrypted Text: {decrypted_text}")
