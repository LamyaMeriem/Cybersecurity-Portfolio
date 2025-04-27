from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from pathlib import Path
from mylib.utile import open_file, save_file



def decrypt_file(data, private_key, filename):

  
  try:
    decrypted_data = private_key.decrypt(
          data,
          padding.OAEP(
              mgf=padding.MGF1(algorithm=hashes.SHA256()),
              algorithm=hashes.SHA256(),
              label=None
          )
      )
    filename = filename.split('.')[0] + "_decrypted.txt"
    save_file(decrypted_data.decode('utf-8'), filename)
    print(decrypted_data.decode('utf-8'))
  except Exception as e:    
    print(f"Error decrypting file: {e}")


file_read = open_file(encrypted=True)
if file_read is None:
  exit()
else:
  data= file_read[0]
  filename = str(file_read[1])
  print(data)
  private_key = open_file(private_key=True)
  if private_key:
    decrypt_file(data, private_key, filename)
  else:
    print("Private key not found")
    