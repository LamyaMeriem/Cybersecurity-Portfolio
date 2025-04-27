from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization


FILE_PATH = Path("files")
FILE_PATH.mkdir(exist_ok=True)
KEYS_PATH = Path("keys")
KEYS_PATH.mkdir(exist_ok=True)
PRIVATE_KEY_FILE = KEYS_PATH/"private_key.pem"
PUBLIC_KEY_FILE = KEYS_PATH/"public_key.pem"



# function that asks the user to enter a file name and returns the content of the file
def open_file(with_hash=False, encrypted=False, public_key=False, private_key=False):
  if public_key:
    filename = PUBLIC_KEY_FILE
  elif private_key:
    filename = PRIVATE_KEY_FILE
  else:
    filename = input("Enter file name: ")
    if not filename.endswith(".txt"):
      filename += ".txt"
      if with_hash:
        filename += ".hash"
      if encrypted:
        filename += ".enc"
    filename = FILE_PATH/filename
  
  try:
    with open(filename, 'rb') as f:
      if public_key:
        public_key = serialization.load_pem_public_key(f.read())
        return public_key
      if private_key:
        private_key = serialization.load_pem_private_key(f.read(), password=None)
        return private_key
      data = f.read()
      if len(data) == 0:
        print(f"\033[91mError: File '{filename}' is empty.\033[0m")
      return data, filename
  except FileNotFoundError:
    print(f"\033[91mError: File named : '{filename}' not found.\033[0m")
    return
  

# function that takes a file and data as argument and write data in this file
def save_file(data, filename, encrypted=False):
  try:
    mode = 'wb' if encrypted else 'w'
    with open(filename, mode) as f:
      f.write(data)
    print(f"\033[92m file saved to {filename}\033[0m")
  except Exception as e:  
    print(f"\033[91m Error saving data to {filename}: {e}\033[0m")


