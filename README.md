# Caesar Cipher

A Python script that implements the Caesar cipher encryption and decryption technique. The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down or up the alphabet.

## Features

- Encrypts plaintext messages using a specified shift value.
- Decrypts ciphertext messages using the same shift value.
- Preserves non-alphabetic characters (such as spaces and punctuation) in the message.

## Usage

1. **Clone the Repository**:
   ```
   git clone https://github.com/yourusername/caesar-cipher.git
   cd caesar-cipher
   ```

2. **Run the Script**:
   - Navigate to the project directory and run the script with Python.

   ```
   python caesar_cipher.py
   ```

3. **Follow the Prompts**:
   - Choose whether to encrypt or decrypt a message.
   - Enter a positive integer shift value (the number of positions to shift each character in the alphabet).
   - Input the message to be processed.

4. **Output**:
   - The script will print the encrypted or decrypted message based on your input.

## Example

Encrypting a message with a shift of 3:
```
Welcome to the Caesar Cipher!
Enter 'encrypt' or 'decrypt': encrypt
Enter the shift value (positive integer): 3
Enter the message: Hello, World!
Encrypted message: Khoor, Zruog!
```

Decrypting the same message with a shift of 3:
```
Enter 'encrypt' or 'decrypt': decrypt
Enter the shift value (positive integer): 3
Enter the message: Khoor, Zruog!
Decrypted message: Hello, World!
```