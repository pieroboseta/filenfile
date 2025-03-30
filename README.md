# **filenfile** 🗄️🔒

## 🚀 Overview
**filenfile** is a simple and easy-to-use Python application that lets you securely hide and extract files and folders inside a main file. The app uses encryption and compression to keep your data safe and hidden from view. You can store files inside a "main file" without anyone knowing, and later extract them when needed. It’s perfect for those who want to keep their sensitive data private! 🕵️‍♂️💻

---

## 🌟 Features
- **Hide Files and Folders**: Securely hide files or entire folders inside a main file.
- **Compression & Encryption**: Files are compressed to save space and encrypted to keep your data safe.
- **Metadata Handling**: Information about hidden files is encrypted and stored separately.
- **User-Friendly GUI**: A beautiful and simple graphical interface built with Tkinter.

---

## 💡 Requirements
To use **filenfile**, you need:
- **Python 3.6+** installed on your computer.
- The following Python libraries:
  - `cryptography`
  - `tkinter` (usually pre-installed with Python)

To install the required libraries, run:
```bash
pip install cryptography
```

---

## 🛠️ Installation Guide

### Step 1: Clone the Repository
You can download the code directly from GitHub by cloning the repository or simply downloading it as a ZIP file.

### Step 2: Install Dependencies
Open a terminal or command prompt, then install the necessary libraries by running:
```bash
pip install cryptography
```

### Step 3: Run the Application
Once everything is installed, you can run the application by executing:
```bash
python filenfile.py
```

---

## 🧑‍💻 How It Works

### Files and Folders Encryption 🔐
1. **Main File**: This is the file where your hidden files will be stored. Choose any file you want (it could be a photo, text file, etc.).
2. **Compression**: We compress files and folders to make them smaller before hiding them.
3. **Encryption**: We use encryption to keep your data safe and unreadable to others.
4. **Metadata**: We store all details about the hidden files (like their names) in a special file, but it’s encrypted too!

### Hiding Files/Folders 🎁
1. **Select a Main File**: Choose the file where the hidden files will be stored.
2. **Hide a File**: Pick a file you want to hide. It will be encrypted, compressed, and safely stored.
3. **Hide a Folder**: Choose a folder to hide. It will be compressed into a `.tar.lzma` file and encrypted.
4. **Extract Files**: You can extract all hidden files and folders whenever you need them by decrypting and decompressing them!

---

## 📜 Usage Instructions

1. **Run the Application**:
   After running `python filenfile.py`, a window will open with a simple interface.

2. **Select Source**:
   - Click **"Select Source"** to choose the main file (where the hidden files will be stored).
   
3. **Hide Files**:
   - Click **"Merge File"** to hide a single file.
   
4. **Hide Folders**:
   - Click **"Compress Folder"** to hide a folder (it will be compressed and encrypted).
   
5. **Extract Files**:
   - Click **"Extract"** to retrieve all hidden files and folders.

### Example 💡:
1. Choose a **main file** (could be anything like `example.txt`).
2. Hide a file, like a sensitive document (`secret.txt`).
3. Or, hide a whole folder (`ImportantDocs`).
4. Later, you can click **Extract** and get everything back!

---

## 🎨 GUI Design

The **filenfile** app has an easy-to-use graphical interface built with **Tkinter**:

- A **dark-themed** interface for a sleek look 🖤
- Easy-to-read buttons with clear labels 🖱️
- A simple layout to guide you through hiding and extracting files

---

## 🧰 How to Modify or Extend
1. **Encryption Key**: The encryption key is saved in `filenfile/encryption_key.key`. You can modify this key if needed.
2. **Compression Options**: Currently, files are compressed with LZMA, but you can change that to any other method.
3. **Metadata**: The metadata about hidden files is stored in `filenfile/hidden_metadata.bin` in an encrypted format.

---

## 🔒 Security Notes
- **Keep the Encryption Key Safe**: If you lose or delete the encryption key (`filenfile/encryption_key.key`), **you won’t be able to recover your hidden files**.
- **Don’t Lose the Metadata File**: The metadata (`filenfile/hidden_metadata.bin`) is also crucial for extracting files.

---

## 🛑 Troubleshooting

### Common Issues 🤔:
1. **No Hidden Files**: Make sure you’ve hidden files or folders before trying to extract them.
2. **Missing Files**: If the key or metadata is deleted, you won't be able to recover your hidden files.
3. **Compression Issues**: Ensure that the files/folders you're trying to hide aren’t in use by another program.

---

## 📝 License
This project is licensed under the MIT License. Feel free to use, modify, and share!

---

## 🙏 Credits
- Uses **cryptography** for encryption/decryption 🔐.
- Built with **Tkinter** for the GUI 🎨.

---

## 👫 Contributing
We welcome contributions! If you find any issues or want to add new features, feel free to **fork** the repo and submit a **pull request**.

---

## 🧑‍💻 Want to Improve the App?
If you want to improve this app (like adding new features or fixing bugs), open an **issue** or submit a **pull request**! All contributions are welcome. 🌟

---

## 💬 Feedback & Support
If you have any questions, feedback, or suggestions, feel free to **open an issue** in the GitHub repository. We’re here to help!

---

Enjoy using **filenfile** and keep your files safe! 🔐✨
