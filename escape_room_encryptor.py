import subprocess

# Prompt for the secret message to encrypt
secret_message = input("Secret Message: ")

# Write the secret message to a file so that it can be used with rizzsec
with open("secret_message.txt", "w") as f:
    f.write(secret_message)

# Encrypt the secret message and saving it to secret.enc
subprocess.run("./rizzsec/rizzsec encrypt -d ./secret_message.txt -i ./key.key -o ./secret.enc", shell=True)

# Read secret.enc to enc_secret
enc_secret = ""
with open("secret.enc", "r") as f:
    enc_secret = f.read()

# Give the secret message to the user
if enc_secret:
    print(f"Encrypted: {enc_secret}")
else: 
    print("error")