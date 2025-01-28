from rizzsec import cryptor

secret = input("Secret: ")

enc_secret = cryptor.encrypt(secret)

print(f"Encrypted: {enc_secret}\n")
