def char_to_num(char):
    return ord(char) - ord('A')

def num_to_char(num):
    return chr(num + ord('A'))

def mod_inv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError("No modular inverse exists")

def determinant(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0])) % 26

def adjugate(matrix):
    adj = [[0] * 3 for _ in range(3)]
    adj[0][0] = matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1]
    adj[0][1] = matrix[0][2] * matrix[2][1] - matrix[0][1] * matrix[2][2]
    adj[0][2] = matrix[0][1] * matrix[1][2] - matrix[0][2] * matrix[1][1]
    adj[1][0] = matrix[1][2] * matrix[2][0] - matrix[1][0] * matrix[2][2]
    adj[1][1] = matrix[0][0] * matrix[2][2] - matrix[0][2] * matrix[2][0]
    adj[1][2] = matrix[0][2] * matrix[1][0] - matrix[0][0] * matrix[1][2]
    adj[2][0] = matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]
    adj[2][1] = matrix[0][1] * matrix[2][0] - matrix[0][0] * matrix[2][1]
    adj[2][2] = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    return adj

def matrix_mod_inv(matrix, mod):
    det = determinant(matrix)
    if det == 0:
        raise ValueError("The key matrix is not invertible (determinant is 0)")
    
    det_inv = mod_inv(det, mod)
    adj = adjugate(matrix)
    inv_matrix = [[(adj[row][col] * det_inv) % mod for col in range(3)] for row in range(3)]
    return inv_matrix

def hill_cipher_encrypt(plaintext, key_matrix):
    n = len(key_matrix)
    plaintext = plaintext.upper().replace(" ", "")
    plaintext_vector = [char_to_num(char) for char in plaintext]
    while len(plaintext_vector) % n != 0:
        plaintext_vector.append(char_to_num('X'))  # Padding with 'X'

    ciphertext = ""
    for i in range(0, len(plaintext_vector), n):
        block = plaintext_vector[i:i + n]
        encrypted_block = [(sum(key_matrix[row][k] * block[k] for k in range(n)) % 26) for row in range(n)]
        ciphertext += ''.join(num_to_char(num) for num in encrypted_block)

    return ciphertext

def hill_cipher_decrypt(ciphertext, key_matrix):
    n = len(key_matrix)
    ciphertext = ciphertext.upper().replace(" ", "")
    ciphertext_vector = [char_to_num(char) for char in ciphertext]
    
    key_matrix_inv = matrix_mod_inv(key_matrix, 26)

    plaintext = ""
    for i in range(0, len(ciphertext_vector), n):
        block = ciphertext_vector[i:i + n]
        decrypted_block = [(sum(key_matrix_inv[row][k] * block[k] for k in range(n)) % 26) for row in range(n)]
        plaintext += ''.join(num_to_char(num) for num in decrypted_block)

    return plaintext

def get_key_matrix(n):
    print(f"Enter the {n}x{n} key matrix row by row (space-separated numbers):")
    key_matrix = []
    for _ in range(n):
        row = list(map(int, input().split()))
        key_matrix.append(row)
    return key_matrix

# Input and Execution
n = int(input("Enter the size of the key matrix (e.g., 3 for 3x3): "))
key_matrix = get_key_matrix(n)
plaintext = input("Enter the plaintext: ")
ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
print("Ciphertext:", ciphertext)

ciphertext = input("Enter the ciphertext: ")
decrypted_text = hill_cipher_decrypt(ciphertext, key_matrix)
print("Decrypted Text:", decrypted_text)