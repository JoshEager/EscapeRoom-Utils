from crypt import cryptor

enc_secret = input("Encrypted: ")

secret = cryptor.decrypt(enc_secret)

print(f"Decrypted: {secret}\n")
