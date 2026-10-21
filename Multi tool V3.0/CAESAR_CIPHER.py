"""
Caesar Cipher Module for Encoding and Decoding text.
"""

def encode_caesar():
    print("\n\n" + "-" * 46 + "\n\n")
    print("     [4-1] ENCODE TEXT (CAESAR CIPHER)")
    print("\n\n" + "-" * 46 + "\n\n")
    text = input('\nEnter text to encode: ')
    print("\n\n")
    
    while True:    
        try:
            shift = int(input('Enter shift value (Example: 3): '))
            print("\n\n")
            break
        except ValueError:
            print('[!] Invalid shift value. Please enter an integer.\n\n')
    
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start + shift) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char)

    encrypted_text = ''.join(result)
    print("\n\n--- Encrypted text (result) ---\n\n")
    print(f'Encrypted text:\n\n\n\n    (    {encrypted_text}    )\n\n')


def decode_caesar():
    print("\n\n" + "-" * 46 + "\n\n")
    print("     [4-2] DECODE TEXT (CAESAR CIPHER)")
    print("\n\n" + "-" * 46 + "\n\n")
    text = input('\nEnter text to decode: ')
    print("\n\n")

    while True:
        try:
            shift = int(input('Enter shift value (Example: 3): '))
            print("\n\n")
            break
        except ValueError:
            print('[!] Invalid shift value. Please enter an integer.\n\n')

    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - start - shift) % 26 + start)
            result.append(shifted_char)
        else:
            result.append(char)

    decrypted_text = ''.join(result)
    print("\n\n--- Decrypted text (result) ---\n\n")
    print(f'Decrypted text:\n\n\n    {decrypted_text}\n\n')


def x():
    """
    Main loop for Caesar Cipher module.
    """
    while True:
        print("\n\n" + "-" * 46 + "\n\n")
        print("    Encode and Decode text (CAESAR CIPHER)")
        print("\n\n" + "-" * 46 + "\n\n")
        print("  [1] ENCODE TEXT (CAESAR CIPHER)")
        print("  [2] DECODE TEXT (CAESAR CIPHER)")
        print("  [0] Back to Main Menu")
        print("\n\n" + "-" * 46 + "\n\n")

        user_choice = input("\n\nSelect an option (0-2): ").strip()
        print("\n")
        
        if user_choice == "1":
            encode_caesar()
        elif user_choice == "2":
            decode_caesar()
        elif user_choice == "0":
            break
        else:
            print("\n\n[Error404] Invalid selection. Please enter a number from 0 to 2.")


if __name__ == "__main__":
    x()
