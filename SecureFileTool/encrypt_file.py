from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from mylib.utile import open_file, save_file
from pathlib import Path

FILE_PATH = Path("files")
FILE_PATH.mkdir(exist_ok=True)

def encrypt_file(data, public_key, filename):
    try:
        encrypted_data = public_key.encrypt(data,
                                                padding.OAEP(
                                                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                    algorithm=hashes.SHA256(),
                                                    label=None  
                                                ))
        save_file(encrypted_data, filename + ".enc", encrypted=True)
    except Exception as e:
        print(f"Error encrypting file: {e}")

file_read = open_file()
if file_read is None:
  exit()
else:
    data= file_read[0]
    filename = "exemple.txt.enc"
    public_key = open_file(public_key=True)

    if public_key:
        encrypt_file(data, public_key, filename)
    else:
        print("Public key not found")



