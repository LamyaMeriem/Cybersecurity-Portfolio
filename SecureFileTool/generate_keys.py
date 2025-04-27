from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path
from mylib.utile import save_file

KEY_SIZE = 2048
PUBLIC_EXPONENT = 65537
KEYS_PATH = Path("keys")
KEYS_PATH.mkdir(exist_ok=True)
PRIVATE_KEY_FILE = KEYS_PATH/"private_key.pem"
PUBLIC_KEY_FILE = KEYS_PATH/"public_key.pem"


def generate_key_pair(key_size, public_exponent):
  print(f"Generating {KEY_SIZE}-bit RSA key pair")
  private_key = rsa.generate_private_key(
    public_exponent=public_exponent,
    key_size=key_size
  )
  public_key = private_key.public_key()
  print("RSA key pair generated")
  return private_key, public_key
  
private_key , public_key = generate_key_pair(KEY_SIZE, PUBLIC_EXPONENT)
try:
  private_key_pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.TraditionalOpenSSL,
    encryption_algorithm=serialization.NoEncryption()
  )
  save_file(private_key_pem, PRIVATE_KEY_FILE, encrypted=True)
except Exception as e:
  print(f"Error: {e}")

try:
  public_key_pem = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
  )
  save_file(public_key_pem, PUBLIC_KEY_FILE, encrypted=True)
except Exception as e:
  print(f"Error: {e}")
