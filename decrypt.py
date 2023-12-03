from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import base64
import tkinter as tk
from tkinter import filedialog, simpledialog

class FileEncryptor:
    def __init__(self, key):
        self.key = key

    def decrypt_file(self, encrypted_file_path):
        with open(encrypted_file_path, 'r') as file:
            file_content = file.read()
        iv, ct = file_content.split('\n')
        iv = base64.b64decode(iv)
        ct = base64.b64decode(ct)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), AES.block_size)
        decrypted_file_path = encrypted_file_path.replace('.enc', '.dec.py')
        with open(decrypted_file_path, 'wb') as file:
            file.write(pt)
        return decrypted_file_path

def select_file_and_decrypt():
    root = tk.Tk()
    root.withdraw()  
    encrypted_file_path = filedialog.askopenfilename(filetypes=[("Encrypted files", "*.enc")])
    if encrypted_file_path:
        key = simpledialog.askstring("Input Key", "Enter the decryption key:", show='*')
        if key:
            key = base64.b64decode(key)
            file_encryptor = FileEncryptor(key)
            decrypted_file = file_encryptor.decrypt_file(encrypted_file_path)
            print(f"Decrypted file: {decrypted_file}")

select_file_and_decrypt()
