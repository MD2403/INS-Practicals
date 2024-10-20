# Encryption Function
def rail_fence_encrypt(text, key):
    rail = [['\n' for _ in range(len(text))] for _ in range(key)]
    dir_down = False
    row, col = 0, 0

    # Placing characters in the zigzag pattern
    for char in text:
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = char
        col += 1
        row = row + 1 if dir_down else row - 1

    # Collecting encrypted text from the rail matrix
    result = [rail[i][j] for i in range(key) for j in range(len(text)) if rail[i][j] != '\n']
    return "".join(result)


# Decryption Function
def rail_fence_decrypt(cipher, key):
    rail = [['\n' for _ in range(len(cipher))] for _ in range(key)]
    dir_down = None
    row, col = 0, 0

    # Marking the zigzag path with '*'
    for _ in range(len(cipher)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        rail[row][col] = '*'
        col += 1
        row = row + 1 if dir_down else row - 1

    # Filling the rail matrix with characters from the cipher text
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    # Reading the decrypted text in a zigzag manner
    result = []
    row, col = 0, 0
    for _ in range(len(cipher)):
        if row == 0 or row == key - 1:
            dir_down = not dir_down
        if rail[row][col] != '\n':
            result.append(rail[row][col])
            col += 1
        row = row + 1 if dir_down else row - 1

    return "".join(result)


# Input and Execution
text = input("Enter the text to be encrypted: ")
key = int(input("Enter the key: "))
encrypted_text = rail_fence_encrypt(text, key)
print(f"Encrypted Text: {encrypted_text}")

cipher = input("Enter the text to be decrypted: ")
key = int(input("Enter the key: "))
decrypted_text = rail_fence_decrypt(cipher, key)
print(f"Decrypted Text: {decrypted_text}")
