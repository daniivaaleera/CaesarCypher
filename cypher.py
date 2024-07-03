import pyperclip

def caesarCypher(text, shift, mode):
    result = []
    for char in text:
        if char.isalpha():
            if char.islower():
                base = ord('a')
            else:
                base = ord('A')
        
        
            if mode == 'Encrypt':
                translatedChar = (ord(char) - base + shift) % 26 + base
            if mode == 'Decrypt':
                translatedChar = (ord(char) - base - shift) % 26 + base
            result.append(chr(translatedChar))
        else:
            result.append(char)   

    return ''.join(result)

def main():
    print("Welcome to the Caesar Cypher script!")
    mode = input("Enter 'Encrypt' or 'Decrypt' to choose the mode: ")
    if mode not in ['Encrypt', 'Decrypt']:
        print("Invalid mode. Please, enter 'encrypt' or 'decrypt': ")
        return
    shift = int(input("Enter the shift value: "))
    message = input("Enter your message: ")

    if mode == 'encrypt':
        encryptedMessage = caesarCypher(message, shift, mode)
        pyperclip.copy(encryptedMessage)
        print(f"Encrypted message: {encryptedMessage}. Copied to the clipboard.")
    else:
        decryptedMessage = caesarCypher(message, shift, mode)
        pyperclip.copy(decryptedMessage)
        print(f"Decrypted message: {decryptedMessage}. Copied to the clipboard.")

if __name__ == "__main__":
    main()
