def row_column_encrypt(text, key):
    rows = (len(text) + key - 1) // key
    grid = [['' for _ in range(key)] for _ in range(rows)]
    index = 0
    for r in range(rows):
        for c in range(key):
            if index < len(text):
                grid[r][c] = text[index]
                index += 1
            else:
                grid[r][c] = ''
    ciphertext = ''
    for c in range(key):
        for r in range(rows):
            if grid[r][c] != '':
                ciphertext += grid[r][c]
    return ciphertext
text = input("Enter the plaintext: ")
key = int(input("Enter the number of columns (key): "))
encrypted_text = row_column_encrypt(text, key)
print(f"Encrypted Text: {encrypted_text}")


#Decryption

def row_column_decrypt(ciphertext, key):
    rows = (len(ciphertext) + key - 1) // key
    grid = [['' for _ in range(key)] for _ in range(rows)]
    index = 0
    for c in range(key):
        for r in range(rows):
            if index < len(ciphertext):
                grid[r][c] = ciphertext[index]
                index += 1
            else:
                grid[r][c] = ''
    plaintext = ''
    for r in range(rows):
        for c in range(key):
            if grid[r][c] != '':
                plaintext += grid[r][c]
    return plaintext
ciphertext = input("Enter the ciphertext: ")
key = int(input("Enter the number of columns (key): "))
decrypted_text = row_column_decrypt(ciphertext, key)
print(f"Decrypted Text: {decrypted_text}")

