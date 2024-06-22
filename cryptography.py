def vigenere_encrypt(plaintext, keyword):
    # Convert the keyword to uppercase
    keyword = keyword.upper()
    # Repeat the keyword to match the length of the plaintext
    keyword_repeated = ''.join([keyword[i % len(keyword)] for i in range(len(plaintext))])
    ciphertext = []
    for p, k in zip(plaintext, keyword_repeated): # zip function is used to iterate over two or more lists, For example, zip("HELLO", "KEYKE") would yield pairs like ('H', 'K'), ('E', 'E'), and so on.
        # Convert characters to their ASCII values, perform encryption, and convert back to characters
        c = (ord(p.upper()) + ord(k)) % 26
        ciphertext.append(chr(c + 65)) # chr() function is used to convert an integer to its corresponding ASCII character. For example, chr(65) would yield 'A', chr(97) would yield 'a', and so on.
    # Join the list of characters into a single string
    return ''.join(ciphertext)

def vigenere_decrypt(ciphertext, keyword):
    # Convert the keyword to uppercase
    keyword = keyword.upper()
    # Repeat the keyword to match the length of the ciphertext
    keyword_repeated = ''.join([keyword[i % len(keyword)] for i in range(len(ciphertext))])
    plaintext = []
    for c, k in zip(ciphertext, keyword_repeated):
        # Convert characters to their ASCII values, perform decryption, and convert back to characters
        p = (ord(c) - ord(k)) % 26
        plaintext.append(chr(p + 65))
    # Join the list of characters into a single string
    return ''.join(plaintext)

def vernam_encrypt(plaintext, binary_key):
    # Convert plaintext to binary representation
    plaintext_binary = ''.join(format(ord(char), '08b') for char in plaintext) # '08b' specifies a binary string of 8 bits, and 'ord' is a function that returns the integer representation of a character in the given encoding.
    # XOR binary plaintext with binary key
    encrypted_binary = ''.join(str(int(p) ^ int(k)) for p, k in zip(plaintext_binary, binary_key))
    # Convert the binary result back to text
    ciphertext = ''.join(chr(int(encrypted_binary[i:i+8], 2)) for i in range(0, len(encrypted_binary), 8))
    return ciphertext

def vernam_decrypt(ciphertext, binary_key):
    # Convert ciphertext to binary representation
    ciphertext_binary = ''.join(format(ord(char), '08b') for char in ciphertext)
    # XOR binary ciphertext with binary key
    decrypted_binary = ''.join(str(int(c) ^ int(k)) for c, k in zip(ciphertext_binary, binary_key))
    # Convert the binary result back to text
    plaintext = ''.join(chr(int(decrypted_binary[i:i+8], 2)) for i in range(0, len(decrypted_binary), 8)) # i:i+8 means we are taking 8 characters starting from index i, and The second argument, 2, tells int to interpret the string as a binary number (base 2)
    return plaintext

def main():
    # Prompt the user to choose the cipher method
    print("Choose cipher method:")
    print("1. Vigenère Cipher")
    print("2. Vernam Cipher")
    cipher_choice = int(input("Enter your choice (1 or 2): "))

    if cipher_choice == 1:
        print("\nFor Vigenère Cipher:")
        print("Choose operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        operation_choice = int(input("Enter your choice (1 or 2): "))
        
        if operation_choice == 1:
            # Get plaintext and keyword from the user
            plaintext = input("Enter plaintext: ").upper()
            keyword = input("Enter keyword: ").upper()
            # Encrypt the plaintext using the Vigenère cipher
            ciphertext = vigenere_encrypt(plaintext, keyword)
            print("Ciphertext:", ciphertext)
        
        elif operation_choice == 2:
            # Get ciphertext and keyword from the user
            ciphertext = input("Enter ciphertext: ").upper()
            keyword = input("Enter keyword: ").upper()
            # Decrypt the ciphertext using the Vigenère cipher
            plaintext = vigenere_decrypt(ciphertext, keyword)
            print("Plaintext:", plaintext)
    
    elif cipher_choice == 2:
        print("\nFor Vernam Cipher:")
        print("Choose operation:")
        print("1. Encrypt")
        print("2. Decrypt")
        operation_choice = int(input("Enter your choice (1 or 2): "))
        
        if operation_choice == 1:
            # Get plaintext and binary key from the user
            plaintext = input("Enter plaintext: ")
            binary_key = input("Enter binary key: ")
            if len(binary_key) != len(plaintext) * 8:
                # Check if binary key length is valid
                print("Error: Binary key length must be equal to 8 times the length of the plaintext.")
            else:
                # Encrypt the plaintext using the Vernam cipher
                ciphertext = vernam_encrypt(plaintext, binary_key)
                print("Ciphertext:", ciphertext)
        
        elif operation_choice == 2:
            # Get ciphertext and binary key from the user
            ciphertext = input("Enter ciphertext: ")
            binary_key = input("Enter binary key: ")
            if len(binary_key) != len(ciphertext) * 8:
                # Check if binary key length is valid
                print("Error: Binary key length must be equal to 8 times the length of the ciphertext.")
            else:
                # Decrypt the ciphertext using the Vernam cipher
                plaintext = vernam_decrypt(ciphertext, binary_key)
                print("Plaintext:", plaintext)

if __name__ == "__main__":
    main()
