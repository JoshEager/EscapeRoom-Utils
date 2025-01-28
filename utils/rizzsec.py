import subprocess
import tempfile
import os
from key import KEYPATH

class Cryptor:
    def __init__(self, keypath: str):
        self.keypath = keypath
        self.path = os.path.dirname(os.path.abspath(__file__))
    
    def encrypt(self, secret: str) -> str:
        with tempfile.TemporaryDirectory() as tmp_dir:
            secret_file = os.path.join(tmp_dir, "secret_file.txt")
            enc_file = os.path.join(tmp_dir, "enc_file.txt")

            with open(secret_file, "w") as f:
                f.write(secret)

            subprocess.run(f"{self.path}/../rizzsec/rizzsec encrypt -d {secret_file} -i {self.path}/{self.keypath} -o {enc_file}", shell=True, check=True)

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

            subprocess.run(f"{self.path}/../rizzsec/rizzsec decrypt -d {enc_file} -i {self.path}/{self.keypath} -o {secret_file}", shell=True, check=True)

            secret_str = ""
            with open(secret_file, "r") as f:
                secret_str = f.read()

            return secret_str
        
cryptor = Cryptor(KEYPATH)
