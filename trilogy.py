from cryptography.fernet import Fernet

key = Fernet.generate_key()
base = Fernet(key)

decrypter = f"""from cryptography.fernet import Fernet

key = {key}
base = Fernet(key)
"""

class trilogy(object):
    def __init__(self, file):
        self.file = file

    def encrypt(self):
        with open(self.file, 'rb') as f:
            data = f.read()

        with open("encrypted.py", "a") as f:
            f.write(decrypter)

        with open("encrypted.py", 'ab') as f:
            f.write(b"c = base.decrypt(b'")
            f.write(base.encrypt(data))
            f.write(b"')" + b"\n")
            f.write(b"exec(" + b"c" + b")")