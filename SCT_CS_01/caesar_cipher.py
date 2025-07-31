def encrypt_text(text, shift):
    """
    Encrypts text using Caesar cipher with given shift value
    
    Args:
        text (str): Text to encrypt
        shift (int): Number of positions to shift
    
    Returns:
        str: Encrypted text
    """
    encrypted = ""
    
    for char in text:
        if char.isalpha():  # Check if character is a letter
            # Get ASCII value and determine if uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            
            # Apply Caesar cipher formula
            encrypted_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            encrypted += encrypted_char
        else:
            # Keep non-alphabetic characters unchanged
            encrypted += char
    
    return encrypted

def decrypt_text(text, shift):
    """
    Decrypts text using Caesar cipher with given shift value
    
    Args:
        text (str): Text to decrypt
        shift (int): Number of positions to shift back
    
    Returns:
        str: Decrypted text
    """
    # Decryption is just encryption with negative shift
    return encrypt_text(text, -shift)

def get_valid_shift():
    """
    Gets valid shift value from user input
    
    Returns:
        int: Valid shift value
    """
    while True:
        try:
            shift = int(input("Enter shift value (1-25): "))
            if 1 <= shift <= 25:
                return shift
            else:
                print("Please enter a number between 1 and 25.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Main program function - handles user interface
    """
    print("=" * 50)
    print("         CAESAR CIPHER PROGRAM")
    print("=" * 50)
    
    while True:
        print("\nChoose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == '1':
            # Encryption
            text = input("\nEnter text to encrypt: ")
            shift = get_valid_shift()
            
            encrypted = encrypt_text(text, shift)
            
            print(f"\nOriginal text: {text}")
            print(f"Shift value: {shift}")
            print(f"Encrypted text: {encrypted}")
            
        elif choice == '2':
            # Decryption
            text = input("\nEnter text to decrypt: ")
            shift = get_valid_shift()
            
            decrypted = decrypt_text(text, shift)
            
            print(f"\nEncrypted text: {text}")
            print(f"Shift value: {shift}")
            print(f"Decrypted text: {decrypted}")
            
        elif choice == '3':
            print("\nThank you for using Caesar Cipher Program!")
            print("Developed as part of SkillCraft Technology Internship")
            break
            
        else:
            print("\nInvalid choice! Please enter 1, 2, or 3.")
        
        # Ask if user wants to continue
        continue_choice = input("\nDo you want to perform another operation? (y/n): ").lower()
        if continue_choice != 'y':
            print("\nThank you for using Caesar Cipher Program!")
            print("Developed as part of SkillCraft Technology Internship")
            break

# Test function to verify the program works correctly
def test_caesar_cipher():
    """
    Test function to verify Caesar cipher implementation
    """
    print("\n" + "="*30)
    print("TESTING CAESAR CIPHER")
    print("="*30)
    
    # Test cases
    test_cases = [
        ("HELLO", 3, "KHOOR"),
        ("hello", 3, "khoor"),
        ("Hello World!", 5, "Mjqqt Btwqi!"),
        ("XYZ", 3, "ABC"),
        ("abc", 1, "bcd")
    ]
    
    for original, shift, expected in test_cases:
        encrypted = encrypt_text(original, shift)
        decrypted = decrypt_text(encrypted, shift)
        
        print(f"Original: '{original}' | Shift: {shift}")
        print(f"Encrypted: '{encrypted}' | Expected: '{expected}'")
        print(f"Decrypted: '{decrypted}' | Match: {original == decrypted}")
        print(f"Encryption Correct: {encrypted == expected}")
        print("-" * 40)

if __name__ == "__main__":
    # Run tests first (optional - comment out for normal use)
    # test_caesar_cipher()
    
    # Run main program
    main()