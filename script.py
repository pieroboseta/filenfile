import os
import json
import lzma
import base64
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox
from cryptography.fernet import Fernet

# Ensure filenfile directory exists
os.makedirs("filenfile", exist_ok=True)

# Hidden metadata and key file inside "filenfile" directory
META_FILE = "filenfile/hidden_metadata.bin"
KEY_FILE = "filenfile/encryption_key.key"
main_file = None  # Global variable to store the selected main file

def generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return Fernet(f.read())
    
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return Fernet(key)

def load_metadata():
    if not os.path.exists(META_FILE):
        return {}
    
    with open(META_FILE, "rb") as f:
        data = f.read()
    
    cipher = generate_key()
    try:
        return json.loads(cipher.decrypt(data).decode())
    except:
        return {}

def save_metadata(metadata):
    cipher = generate_key()
    with open(META_FILE, "wb") as f:
        encrypted_data = cipher.encrypt(json.dumps(metadata).encode())
        f.write(encrypted_data)

def select_main_file():
    global main_file
    main_file = filedialog.askopenfilename(filetypes=[("All Files", "*.*")])
    if main_file:
        messagebox.showinfo("Main File Selected", f"Data will be stored in: {os.path.basename(main_file)}")

def hide_file():
    if not main_file:
        messagebox.showerror("Error", "Select a main file first!")
        return
    
    file_to_hide = filedialog.askopenfilename()
    if not file_to_hide:
        return
    
    with open(file_to_hide, "rb") as f:
        file_data = f.read()
    
    compressed_data = lzma.compress(file_data)  # Improved compression
    cipher = generate_key()
    encrypted_data = cipher.encrypt(compressed_data).decode()
    
    metadata = load_metadata()
    metadata[os.path.basename(file_to_hide)] = encrypted_data
    save_metadata(metadata)
    
    os.remove(file_to_hide)
    messagebox.showinfo("Success", "File hidden successfully!")

def hide_folder():
    if not main_file:
        messagebox.showerror("Error", "Select a main file first!")
        return
    
    folder_to_hide = filedialog.askdirectory()
    if not folder_to_hide:
        return
    
    archive_path = folder_to_hide + ".tar.lzma"
    shutil.make_archive(folder_to_hide, 'tar')
    with open(archive_path, "rb") as f:
        folder_data = f.read()
    os.remove(archive_path)
    
    compressed_data = lzma.compress(folder_data)
    cipher = generate_key()
    encrypted_data = cipher.encrypt(compressed_data).decode()
    
    metadata = load_metadata()
    metadata[os.path.basename(folder_to_hide) + ".tar.lzma"] = encrypted_data
    save_metadata(metadata)
    
    shutil.rmtree(folder_to_hide)
    messagebox.showinfo("Success", "Folder compressed successfully!")

def extract_files():
    if not main_file:
        messagebox.showerror("Error", "Select a main file first!")
        return
    
    metadata = load_metadata()
    if not metadata:
        messagebox.showerror("Error", "No data found in source!")
        return
    
    save_path = filedialog.askdirectory(title="Select folder to extract files")
    if not save_path:
        return
    
    for file_name, encrypted_data in metadata.items():
        cipher = generate_key()
        decrypted_data = cipher.decrypt(encrypted_data.encode())
        decompressed_data = lzma.decompress(decrypted_data)
        
        with open(os.path.join(save_path, file_name), "wb") as f:
            f.write(decompressed_data)
    
    os.remove(META_FILE)  # Clear metadata after extraction
    messagebox.showinfo("Success", "All files extracted successfully!")

def gui():
    root = tk.Tk()
    root.title("filenfile")
    root.geometry("400x300")
    root.configure(bg="#2C2F33")
    
    frame = tk.Frame(root, bg="#2C2F33")
    frame.pack(expand=True)
    
    btn_style = {"font": ("Arial", 12), "width": 15, "height": 2, "bg": "#7289DA", "fg": "white", "bd": 0, "relief": "flat"}
    
    btn_select_main = tk.Button(frame, text="Select Source", command=select_main_file, **btn_style)
    btn_select_main.grid(row=0, column=0, pady=10, padx=20)
    
    btn_hide = tk.Button(frame, text="Merge File", command=hide_file, **btn_style)
    btn_hide.grid(row=1, column=0, pady=10, padx=20)
    
    btn_hide_folder = tk.Button(frame, text="Compress Folder", command=hide_folder, **btn_style)
    btn_hide_folder.grid(row=2, column=0, pady=10, padx=20)
    
    btn_extract = tk.Button(frame, text="Extract", command=extract_files, **btn_style)
    btn_extract.grid(row=3, column=0, pady=10, padx=20)
    
    root.mainloop()

gui()
