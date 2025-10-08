from PIL import Image
import numpy as np


def encrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    encrypted_array = img_array ^ key  # XOR operation
    encrypted_img = Image.fromarray(encrypted_array)
    encrypted_img.save(output_path)
    print("Image encrypted and saved as", output_path)


def decrypt_image(input_path, output_path, key):
    img = Image.open(input_path)
    img_array = np.array(img)
    decrypted_array = img_array ^ key  # XOR operation reverses encryption
    decrypted_img = Image.fromarray(decrypted_array)
    decrypted_img.save(output_path)
    print("Image decrypted and saved as", output_path)

# Example usage:


key = 42  # Choose any integer key between 0 and 255
encrypt_image("Screenshot-9.jpg", "encrypted.png", key)
decrypt_image("encrypted.png", "decrypted.png", key)
