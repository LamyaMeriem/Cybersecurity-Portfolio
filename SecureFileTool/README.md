# SecureFileTool 🔐

SecureFileTool is a set of simple tools developed in Python to perform basic operations related to file security.

It enables you to:

- Generate RSA key pairs (private and public)
- Encrypt a text file using an RSA public key
- Decrypt an encrypted file (.enc) using an RSA private key
- Generate a SHA256 hash of a file
- Verify the integrity of a file by comparing its contents with a supplied SHA256 hash

---

## 📦 Installation

1.  **Run the :** repository

    ```bash
    git clone https://github.com/LamyaMeriem/Cybersecurity-Portfolio.git
    cd Cybersecurity-Portfolio/SecureFileTool
    ```

2.  **Install dependencies:**
    Make sure you have Python and pip installed. Then run :

    ```bash
    pip install -r requirements.txt
    ```

---

## 🛠 Features

The following scripts are available:

| Script | Description |
| :---------------- | :--------------------------------------------------------------- |
| `generate_keys.py`| Generates a pair of RSA keys (private/public) and saves them in the `/keys/` folder. |
| Encrypt_file.py Encrypts a specified `.txt` file with the RSA public key.
| decrypt_file.py` | Decrypts a specified `.enc` file with the RSA private key. |
| `hash_tool.py` | Generates a SHA256 hash for a specified `.txt` file. |
| `check_hash.py` | Checks the integrity of a file by comparing its current hash with an existing `.hash` file.
| `utils.py` | Contains utility functions (file/key loading) used by other scripts. |

---

## 📂 Folder organization

text
SecureFileTool/
├── generate_keys.py # Script to generate RSA keys
├── encrypt_file.py # Script to encrypt a file
├── decrypt_file.py # Script to decrypt a file
├── hash_tool.py # Script to generate the hash of a file
├── check_hash.py # Script to check the hash of a file
├── utils.py # Shared utility functions
├── requirements.txt # List of Python dependencies
├── README.md # This file
├── keys/ # Folder for storing generated keys
│ ├── private_key.pem # Private key (generated)
│ └── public_key.pem # Public key (generated)
└── files/ # Folder for files to be processed
    ├── file.txt # Example of file to be encrypted/hashed
    ├── fichier.txt.enc # Example of encrypted file (generated)
    └── fichier.txt.hash # Example of a hashed file (generated)