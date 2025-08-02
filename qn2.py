def encrypt_decrypt_file(input_file, output_file, key):
    try:
        with open(input_file, 'rb') as f:
            data = f.read()

        encrypted_data = bytearray()
        for byte in data:
            encrypted_data.append(byte ^ key)  # XOR encryption

        with open(output_file, 'wb') as f:
            f.write(encrypted_data)

        print(f"Operation completed. Output saved as: {output_file}")

    except FileNotFoundError:
        print("File not found. Please check the file name and path.")

# Main part
print("1. Encrypt Image")
print("2. Decrypt Image")
choice = input("Enter your choice (1 or 2): ")

file_path = input("Enter image file name (with extension): ")
output_file = "output_image.png"
key = 123  # XOR key (can be any number from 0–255)

if choice == '1':
    encrypt_decrypt_file(file_path, output_file, key)
elif choice == '2':
    encrypt_decrypt_file(file_path, "decrypted_image.png", key)
else:
    print("Invalid choice.")
