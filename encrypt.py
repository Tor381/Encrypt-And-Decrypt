from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import filedialog

def encrypt_file(file_name):
    key = Fernet.generate_key()
    print(f"Encryption Key: {key.decode()}")
    with open(file_name, "rb") as file:
        data = file.read()
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    with open(file_name + ".encrypted", "wb") as file:
        file.write(encrypted_data)

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
encrypt_file(file_path)
input("Press Enter to exit...")