def xor_encrypt_decrypt(data, key):
    out = bytearray()
    for i in range(len(data)):
        out.append(data[i] ^ key[i % len(key)])
    return bytes(out)

# Main program
print("==== FILE ENCRYPTOR / DECRYPTOR ====")
print("1. Encrypt file")
print("2. Decrypt file")
choice = input("Enter your choice (1 or 2): ")

file_name = input("Enter file name (with extension): ")
key_input = input("Enter key: ")

try:
    with open(file_name, "rb") as f:
        file_data = f.read()
except FileNotFoundError:
    print("Bro... file not found. Check the name and try again.")
    exit()

key_bytes = key_input.encode()
result = xor_encrypt_decrypt(file_data, key_bytes)

if choice == "1":
    out_file = "encrypted_" + file_name
elif choice == "2":
    out_file = "decrypted_" + file_name
else:
    print("Invalid choice dude!")
    exit()

with open(out_file, "wb") as f:
    f.write(result)

print("Done! File saved as", out_file)
