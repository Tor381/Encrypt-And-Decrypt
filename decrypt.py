from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

def decrypt_file(file_name, key):
    with open(file_name, "rb") as file:
        encrypted_data = file.read()
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(file_name[:-10], "wb") as file:
        file.write(decrypted_data)

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename(filetypes=[("Encrypted Files", "*.encrypted")])
key = input("Enter the encryption key: ").encode()
decrypt_file(file_path, key)
input("Press Enter to exit...")
