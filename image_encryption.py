import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog

def encrypt_image(image_path, key):
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    if image is None:
        raise ValueError("Image not found or invalid format.")
    
    encrypted_image = np.bitwise_xor(image, key)
    cv2.imwrite("encrypted.png", encrypted_image)
    print("Image encrypted and saved as 'encrypted.png'")

def decrypt_image(encrypted_path, key):
    encrypted_image = cv2.imread(encrypted_path, cv2.IMREAD_UNCHANGED)
    if encrypted_image is None:
        raise ValueError("Encrypted image not found or invalid format.")
    
    decrypted_image = np.bitwise_xor(encrypted_image, key)
    cv2.imwrite("decrypted.png", decrypted_image)
    print("Image decrypted and saved as 'decrypted.png'")

def select_file():
    file_path = filedialog.askopenfilename()
    return file_path

def encrypt_action():
    file_path = select_file()
    if file_path:
        key = int(entry_key.get())
        encrypt_image(file_path, key)

def decrypt_action():
    file_path = select_file()
    if file_path:
        key = int(entry_key.get())
        decrypt_image(file_path, key)

# GUI setup
root = tk.Tk()
root.title("Image Encryption Tool")

tk.Label(root, text="Enter Key:").pack()
entry_key = tk.Entry(root)
entry_key.pack()

tk.Button(root, text="Encrypt Image", command=encrypt_action).pack()
tk.Button(root, text="Decrypt Image", command=decrypt_action).pack()

tk.Button(root, text="Exit", command=root.quit).pack()

root.mainloop()
