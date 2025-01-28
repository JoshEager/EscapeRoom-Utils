import subprocess
import tempfile
import os
from key import KEYPATH

class Cryptor:
    def __init__(self, keypath: str):
        self.keypath = keypath
    
    def encrypt(self, secret: str) -> str:
        with tempfile.TemporaryDirectory() as tmp_dir:
            secret_file = os.path.join(tmp_dir, "secret_file.txt")
            enc_file = os.path.join(tmp_dir, "enc_file.txt")

            with open(secret_file, "w") as f:
                f.write(secret)

            subprocess.run(f"../rizzsec/rizzsec encrypt -d {secret_file} -i {self.keypath} -o {enc_file}")

            enc_str = ""
            with open(enc_file, "r") as f:
                enc_str = f.read()

            return enc_str
        
    def decrypt(self, enc_str: str) -> str:
        with tempfile.TemporaryDirectory() as tmp_dir:
            enc_file = os.path.join(tmp_dir, "enc_file.txt")
            secret_file = os.path.join(tmp_dir, "secret_file.txt")

            with open(enc_file, "w") as f:
                f.write(enc_str)

            subprocess.run(f"../rizzsec/rizzsec decrypt -d {enc_file} -i {self.keypath} -o {secret_file}")

            secret_str = ""
            with open(secret_file, "r") as f:
                secret_str = f.read()

            return secret_str
        
cryptor = Cryptor(KEYPATH)
