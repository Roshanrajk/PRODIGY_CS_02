Unlock simple image encryption and decryption with this Python script! This tool uses XOR operations to modify image files, allowing you to secure or reveal their content with a key.

Key Features

XOR Encryption/Decryption: Alter image bytes using a key. Encrypt by modifying byte values, or decrypt by reversing the process with the same key.
File Handling: Reads and writes images in binary mode, ensuring proper file operations and closure.
User-Friendly: Select encryption or decryption, and input the file path and key when prompted.

How It Works
Select Mode: Choose to encrypt or decrypt the image.
Input Details: Provide the image path and XOR key.
Process: The script reads the image, applies the XOR operation to each byte, and writes the modified data back.
Important Notes
Key Consistency: Use the same key for both encryption and decryption.
Backup: Keep a backup of the original image to prevent data loss.
Security: This method is simple and not for strong data protection.
