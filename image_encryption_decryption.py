def encrypt_decrypt_image(path, key, mode):
    try:
        # Open the file for reading in binary mode
        with open(path, 'rb') as fin:
            image = fin.read()

        # Convert the image into a byte array to perform XOR operation
        image = bytearray(image)

        # Perform XOR operation for encryption/decryption
        for index, value in enumerate(image):
            image[index] = value ^ key

        # Open the file for writing in binary mode
        with open(path, 'wb') as fin:
            fin.write(image)

        print(f'{mode.capitalize()}ion Done...')

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Get user choice for mode
    mode = input("Do you want to (E)ncrypt or (D)ecrypt the image? ").strip().lower()

    if mode not in ['e', 'd']:
        print("Invalid mode selected. Please choose 'E' for encryption or 'D' for decryption.")
    else:
        # Take the path of the image as input
        path = input(r'Enter path of the Image: ').strip()

        # Take the key as input
        key = int(input(f'Enter Key for {mode.capitalize()}ion of Image: ').strip())

        print(f'The path of the file: {path}')
        print(f'Key for {mode.capitalize()}ion: {key}')

        encrypt_decrypt_image(path, key, mode)
