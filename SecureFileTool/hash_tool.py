import hashlib
from mylib.utile import open_file, save_file

# function that takes data as argument and returns its SHA256 hash
def hash_sha256(data):

  print("Hashing file...")
  try:
    hash_value = hashlib.sha256(data).hexdigest()
    save_file(hash_value, str(filename)+ ".hash")
    return hash_value
  except Exception as e:
    print(f"Error hashing file: {e}")


file_read = open_file()
if file_read is None:
  exit()
else:
  data, filename = file_read
  hash_value = hash_sha256(data)
  print(f"Hash of {filename}: {hash_value}")


