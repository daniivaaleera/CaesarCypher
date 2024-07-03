# Caesar Cipher Script

A Python script that implements the Caesar cipher encryption and decryption technique. The Caesar cipher shifts each letter in the plaintext by a fixed number of positions down or up the alphabet.

## Features

- Encrypts plaintext messages using a specified shift value.
- Decrypts ciphertext messages using the same shift value.
- Preserves non-alphabetic characters (such as spaces and punctuation) in the message.
- Copies the encrypted or decrypted message to the clipboard using `pyperclip`.

## Requirements

- Python 3.x
- `pyperclip` library (install via `pip install pyperclip`)

## Usage

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/daniivaaleera/CaesarCypher.git
   cd CaesarCypher
   ```

2. **Install Dependencies**:
   ```bash
   pip install pyperclip
   ```

3. **Run the Script**:
   - Navigate to the project directory and run the script with Python.

   ```bash
   python caesar_cipher.py
   ```

4. **Follow the Prompts**:
   - Choose whether to encrypt or decrypt a message by entering `Encrypt` or `Decrypt`.
   - Enter a positive integer shift value (the number of positions to shift each character in the alphabet).
   - Input the message to be processed.

5. **Output**:
   - The script will print the encrypted or decrypted message based on your input.
   - The result will also be copied to your clipboard for easy pasting.

## Example

Encrypting a message with a shift of 3:
```
Welcome to the Caesar Cipher script!
Enter 'Encrypt' or 'Decrypt' to choose the mode: Encrypt
Enter the shift value: 3
Enter your message: Hello, World!
Encrypted message: Khoor, Zruog!. Copied to the clipboard.
```

Decrypting the same message with a shift of 3:
```
Enter 'Encrypt' or 'Decrypt' to choose the mode: Decrypt
Enter the shift value: 3
Enter your message: Khoor, Zruog!
Decrypted message: Hello, World!. Copied to the clipboard.