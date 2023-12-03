# Encryption Script

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad
import base64
import tkinter as tk
from tkinter import filedialog

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

def select_file_and_encrypt():
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    file_path = filedialog.askopenfilename(filetypes=[("Python files", "*.py")])
    if file_path:
        key = get_random_bytes(16)
        file_encryptor = FileEncryptor(key)
        encrypted_file = file_encryptor.encrypt_file(file_path)
        print(f"Encrypted file: {encrypted_file}")
        print(f"Encryption key (save this!): {base64.b64encode(key).decode()}")

select_file_and_encrypt()
