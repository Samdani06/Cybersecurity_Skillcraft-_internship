def caesar_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result


def caesar_decrypt(ciphertext, shift):
    return caesar_encrypt(ciphertext, -shift)

# User Inputs the Message and the Shift value below.


message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted = caesar_encrypt(message, shift)
decrypted = caesar_decrypt(encrypted, shift)

print(f"Encrypted Message: {encrypted}")
print(f"Decrypted Message: {decrypted}")
