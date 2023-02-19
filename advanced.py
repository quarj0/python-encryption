import random

def caesar_cipher(plaintext, shift):
    """
    Encrypts plaintext using the Caesar cipher with a given shift.

    Parameters:
    plaintext (str): The plaintext to encrypt.
    shift (int): The number of positions to shift each character.

    Returns:
    The encrypted ciphertext (str).
    """
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            # Determine the new character by shifting it by the specified amount
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            new_char = char
        ciphertext += new_char
    return ciphertext

def vigenere_cipher(plaintext, key):
    """
    Encrypts plaintext using the Vigenere cipher with a given key.

    Parameters:
    plaintext (str): The plaintext to encrypt.
    key (str): The encryption key.

    Returns:
    The encrypted ciphertext (str).
    """
    ciphertext = ""
    key_length = len(key)
    for i, char in enumerate(plaintext):
        if char.isalpha():
            # Determine the shift amount based on the corresponding key character
            shift = ord(key[i % key_length]) - 65
            new_char = chr((ord(char) - 65 + shift) % 26 + 65)
        else:
            new_char = char
        ciphertext += new_char
    return ciphertext

def generate_key(length):
    """
    Generates a random encryption key of the specified length.

    Parameters:
    length (int): The length of the key to generate.

    Returns:
    The encryption key (str).
    """
    key = ""
    for i in range(length):
        key += chr(random.randint(65, 90))
    return key

# Example usage
plaintext = "I love you sikapa"
key = generate_key(5)
ciphertext = vigenere_cipher(plaintext, key)
print("Plaintext: ", plaintext)
print("Key: ", key)
print("Ciphertext: ", ciphertext)
