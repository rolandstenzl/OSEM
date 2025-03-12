def caesar_cipher(text, shift, mode='encrypt'):
    """
    A function to encrypt or decrypt a text using the Caesar cipher method.
    
    Parameters:
    text (str): The input text to be encrypted or decrypted.
    shift (int): The number of positions to shift each letter.
    mode (str): 'encrypt' to encrypt the text, 'decrypt' to decrypt it.
    
    Returns:
    str: The transformed text after applying the Caesar cipher.
    """
    result = ""
    
    # Reverse the shift if decrypting
    if mode == 'decrypt':
        shift = -shift  
    
    for char in text:
        # Check if the character is a letter
        if char.isalpha():  
            # Determine if the character is uppercase or lowercase
            shift_base = ord('A') if char.isupper() else ord('a')
            
            # Shift the character and wrap around the alphabet if necessary
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            # Keep non-letter characters unchanged
            result += char  
    
    return result

# Example usage
text = "Hello, World!"  # Input text
shift = 3  # Number of positions to shift

# Encrypt the text
encrypted_text = caesar_cipher(text, shift, 'encrypt')
# Decrypt the text
decrypted_text = caesar_cipher(encrypted_text, shift, 'decrypt')

# Print results
print(f"Original: {text}")
print(f"Encrypted: {encrypted_text}")
print(f"Decrypted: {decrypted_text}")
