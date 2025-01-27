import subprocess

# Get message from user
enc_message = input("Encrypted: ")

# Write the message to a file so it can be used with rizzsec
with open("encrypted.enc", "w") as f:
    f.write(enc_message)

# Use rizzsec to decrypt the message that was encrypted with the key
subprocess.run("./rizzsec/rizzsec decrypt -d ./encrypted.enc -i ./key.key -o decrypted.denc", shell=True)

# Load the contents of the file to decrypted_message
decrypted_message = ""
with open("decrypted.denc", "r") as f:
    decrypted_message = f.read()

# Print decrypted message, with error handling
if decrypted_message:
    print(f"Decrypted: {decrypted_message}")
else:
    print("Error occureed while reading the message!")