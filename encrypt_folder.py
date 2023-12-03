import os
from tkinter import filedialog, Tk
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64

class FileEncryptor:
    def __init__(self, key):
        self.key = key

    def encrypt_file(self, file_path):
        cipher = AES.new(self.key, AES.MODE_CBC)
        with open(file_path, 'rb') as file:
            file_data = file.read()
        ct_bytes = cipher.encrypt(pad(file_data, AES.block_size))
        iv = base64.b64encode(cipher.iv).decode('utf-8')
        ct = base64.b64encode(ct_bytes).decode('utf-8')
        encrypted_file_path = file_path + '.enc'
        with open(encrypted_file_path, 'w') as file:
            file.write(iv + '\n' + ct)
        return encrypted_file_path

def encrypt_all_files_in_directory(directory_path):
    keys_file_path = os.path.join(directory_path, 'encryption_keys.txt')
    with open(keys_file_path, 'w') as keys_file:
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                if file.endswith('.py'):
                    full_file_path = os.path.join(root, file)
                    key = get_random_bytes(16)
                    file_encryptor = FileEncryptor(key)
                    encrypted_file = file_encryptor.encrypt_file(full_file_path)
                    print(f"Encrypted file: {encrypted_file}")
                    encoded_key = base64.b64encode(key).decode()
                    keys_file.write(f"{full_file_path} : {encoded_key}\n")

def select_directory():
    root = Tk()
    root.withdraw()  
    directory_path = filedialog.askdirectory() 
    if directory_path:  
        encrypt_all_files_in_directory(directory_path)

select_directory()
