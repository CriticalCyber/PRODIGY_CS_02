import cv2
import numpy as np

def encrypt_image(image_path, key):
    # Read the image
    image = cv2.imread(image_path)
    height, width, channels = image.shape

    # Create a new image to store the encrypted image
    encrypted_image = np.zeros((height, width, channels), dtype=np.uint8)

    # Perform encryption by swapping pixel values
    for y in range(height):
        for x in range(width):
            for c in range(channels):
                encrypted_image[y, x, c] = image[y, x, c] ^ key

    return encrypted_image

def decrypt_image(encrypted_image, key):
    # Create a new image to store the decrypted image
    decrypted_image = np.zeros(encrypted_image.shape, dtype=np.uint8)

    # Perform decryption by swapping pixel values again
    for y in range(encrypted_image.shape[0]):
        for x in range(encrypted_image.shape[1]):
            for c in range(encrypted_image.shape[2]):
                decrypted_image[y, x, c] = encrypted_image[y, x, c] ^ key

    return decrypted_image

# Main program
image_path = input("Enter the path of the image file: ")
key = int(input("Enter the encryption key (an integer): "))

# Encrypt the image
encrypted_image = encrypt_image(image_path, key)
cv2.imshow("Encrypted Image", encrypted_image)
cv2.waitKey(0)

# Decrypt the image
decrypted_image = decrypt_image(encrypted_image, key)
cv2.imshow("Decrypted Image", decrypted_image)
cv2.waitKey(0)

cv2.destroyAllWindows()