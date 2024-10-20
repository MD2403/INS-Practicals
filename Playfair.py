# key - paru
# text-yash

def prepare_input(input_string):
    input_string = input_string.upper().replace("J", "I")
    input_string = ''.join(filter(str.isalpha, input_string))
    return input_string

def generate_matrix(key):
    key = prepare_input(key)
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    used_chars = set()
    
    for char in key + alphabet:
        if char not in used_chars:
            used_chars.add(char)
            matrix.append(char)
    
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_position(char, matrix):
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == char:
                return row, col
    return None

def playfair_encrypt(plaintext, key):
    plaintext = prepare_input(plaintext)
    matrix = generate_matrix(key)
    if len(plaintext) % 2 != 0:
        plaintext += 'X'
    
    ciphertext = ''
    for i in range(0, len(plaintext), 2):
        a, b = plaintext[i], plaintext[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        
        if row1 == row2:
            ciphertext += matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:
            ciphertext += matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
        else:
            ciphertext += matrix[row1][col2] + matrix[row2][col1]
    
    return ciphertext

key = input("Enter the key: ")
plaintext = input("Enter the plaintext: ")
ciphertext = playfair_encrypt(plaintext, key)
print("Encrypted:", ciphertext)


def playfair_decrypt(ciphertext, key):
    ciphertext = prepare_input(ciphertext)
    matrix = generate_matrix(key)
    
    plaintext = ''
    for i in range(0, len(ciphertext), 2):
        a, b = ciphertext[i], ciphertext[i+1]
        row1, col1 = find_position(a, matrix)
        row2, col2 = find_position(b, matrix)
        
        if row1 == row2:
            plaintext += matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:
            plaintext += matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
        else:
            plaintext += matrix[row1][col2] + matrix[row2][col1]
    
    return plaintext

key = input("Enter the key: ")
ciphertext = input("Enter the ciphertext: ")
decrypted_text = playfair_decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
