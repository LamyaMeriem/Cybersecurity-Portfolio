import hashlib
from mylib.utile import open_file
# function that takes a file and compare his hash with filename.hash


def compare_hash(hash_value, data_file):
  print("Comparing hashes...")

  if data_file == hash_value:
    print("\033[92m✅ Hashes are the same\033[0m")
  else:
    print("\033[91m❌ Hashes are different\033[0m")

file_read_hash = open_file(with_hash=True)
file_read = open_file()
if file_read is None:
  exit()
else:
  data = file_read[0]

if file_read_hash is None:
  exit()
else:
  data_hash = file_read_hash[0]

