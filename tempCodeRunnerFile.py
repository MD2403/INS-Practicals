import random

# # Helper Functions
# def is_prime(n):
#     """Check if a number is prime."""
#     if n <= 1:
#         return False
#     if n <= 3:
#         return True
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# def generate_prime(min_value=2):
#     """Generate a random prime number."""
#     while True:
#         num = random.randint(min_value, 100)
#         if is_prime(num):
#             return num

# def gcd(a, b):
#     """Compute the greatest common divisor of a and b."""
#     while b:
#         a, b = b, a % b
#     return a

# def mod_inverse(a, m):
#     """Find the modular inverse of a under modulo m."""
#     m0, x0, x1 = m, 0, 1
#     if m == 1:
#         return 0
#     while a > 1:
#         q = a // m
#         m, a = a % m, m
#         x0, x1 = x1 - q * x0, x0
#     if x1 < 0:
#         x1 += m0
#     return x1

# # RSA Key Generation
# def generate_keys():
#     """Generate RSA public and private keys."""
#     p = generate_prime()
#     q = generate_prime()
#     while p == q:
#         q = generate_prime()

#     n = p * q
#     phi = (p - 1) * (q - 1)

#     e = random.randrange(2, phi)
#     while gcd(e, phi) != 1:
#         e = random.randrange(2, phi)

#     d = mod_inverse(e, phi)

#     return ((e, n), (d, n))

# # Encryption
# def encrypt(public_key, plaintext):
#     """Encrypt a message using the public key."""
#     e, n = public_key
#     return [pow(ord(char), e, n) for char in plaintext]

# # Main Program for Encryption
# if __name__ == "__main__":
#     # Generate RSA keys
#     public_key, private_key = generate_keys()

#     # Display public and private keys
#     print("Generated Public Key:", public_key)
#     print("Generated Private Key:", private_key)

#     # User input for message
#     message = input("\nEnter the message to encrypt: ")

#     # Encrypt the message
#     encrypted_msg = encrypt(public_key, message)
#     print("\nEncrypted Message:", encrypted_msg)

#     # Save keys and encrypted message to file
#     with open('keys.txt', 'w') as f:
#         f.write(f"Public Key: {public_key}\n")
#         f.write(f"Private Key: {private_key}\n")

#     with open('encrypted_message.txt', 'w') as f:
#         f.write(','.join(map(str, encrypted_msg)))

#     print("\nKeys and encrypted message saved to files.")