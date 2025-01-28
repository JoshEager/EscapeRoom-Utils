import subprocess
from key import KEYPATH

ENCRYPTED_FILE_PATH = "../tmp/escape_room_decryptor_enc.txt"
DECRYPTED_FILE_PATH = "../tmp/escape_room_decryptor_denc.txt"

# Get message from user
enc_message = input("Encrypted: ")

# Write the message to a file so it can be used with rizzsec
with open(ENCRYPTED_FILE_PATH, "w") as f:
    f.write(enc_message)

# Use rizzsec to decrypt the message that was encrypted with the key
subprocess.run(f"../rizzsec/rizzsec decrypt -d {ENCRYPTED_FILE_PATH} -i {KEYPATH} -o {DECRYPTED_FILE_PATH}", shell=True)

# Load the contents of the file to decrypted_message
decrypted_message = ""
with open(DECRYPTED_FILE_PATH, "r") as f:
    decrypted_message = f.read()

# Print decrypted message, with error handling
if decrypted_message:
    print(f"Decrypted: {decrypted_message}\n")
else:
    print("Error occureed while reading the message!")