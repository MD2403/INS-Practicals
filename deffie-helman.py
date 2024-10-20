import random

# Function to perform modular exponentiation
def power(base, exponent, modulus):
    result = 1
    base = base % modulus
    while exponent > 0:
        # If exponent is odd, multiply base with the result
        if exponent % 2 == 1:
            result = (result * base) % modulus
        # Update exponent and base
        exponent = exponent >> 1
        base = (base * base) % modulus
    return result

# Generate Diffie-Hellman key
def diffie_hellman_key_exchange():
    # Publicly known values
    g = 5  # Primitive root
    p = 23 # Prime modulus

    print(f"Publicly shared values: g = {g}, p = {p}")

    # Alice's secret key (random number)
    a = random.randint(1, p-1)
    A = power(g, a, p)  # Alice sends A to Bob
    print(f"Alice's secret key: {a}")
    print(f"Alice's public value A: {A}")

    # Bob's secret key (random number)
    b = random.randint(1, p-1)
    B = power(g, b, p)  # Bob sends B to Alice
    print(f"Bob's secret key: {b}")
    print(f"Bob's public value B: {B}")

    # Alice computes the shared key
    alice_shared_key = power(B, a, p)
    print(f"Alice's shared key: {alice_shared_key}")

    # Bob computes the shared key
    bob_shared_key = power(A, b, p)
    print(f"Bob's shared key: {bob_shared_key}")

    # Verify if both keys are equal
    if alice_shared_key == bob_shared_key:
        print("The shared secret key has been successfully established!")
    else:
        print("Error: The shared keys do not match!")

# Run the Diffie-Hellman key exchange
diffie_hellman_key_exchange()
