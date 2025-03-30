# filenfile

## Overview
**filenfile** is a Python-based application designed to hide and extract files and folders inside a main file using encryption and compression techniques. It allows users to securely store sensitive data in an innocuous file while keeping the original files hidden and encrypted. The metadata about the hidden files is securely stored and encrypted to ensure the contents remain confidential and undetectable.

## Features
- **Hide Files and Folders**: Select files or folders and store them inside a chosen "main file" with encryption and compression for extra security.
- **Extract Hidden Files**: Retrieve hidden files from the main file by decrypting and decompressing them.
- **Compression & Encryption**: Files and folders are compressed with LZMA and encrypted with AES (via `cryptography.fernet`).
- **Metadata Handling**: Hidden file metadata is stored securely and encrypted in a separate metadata file, ensuring easy recovery of hidden files.
- **GUI Interface**: A user-friendly interface built with Tkinter allows for easy file selection, hiding, and extraction.

---

## Requirements
- **Python 3.6+**
- **Libraries**: `os`, `json`, `lzma`, `base64`, `shutil`, `tkinter`, `cryptography`

To install required dependencies, run:
```
pip install cryptography
```

---

## Installation

1. Clone the repository or download the source code.
2. Ensure you have Python 3.6+ installed on your machine.
3. Install the necessary dependencies using `pip`:
   ```
   pip install cryptography
   ```

---

## How it Works

### Files & Folders Encryption
1. **Main File**: A chosen main file that will store the encrypted and compressed data.
2. **Encryption Key**: A unique AES encryption key is generated and stored in a hidden file (`filenfile/encryption_key.key`).
3. **Compression**: Files and folders are compressed using LZMA to minimize size before being encrypted.
4. **Metadata**: All metadata about the hidden files (such as file names and encrypted data) is securely stored in `filenfile/hidden_metadata.bin`. This metadata is encrypted using the same AES encryption key.
5. **Decryption**: When extracting hidden files, the application decrypts the metadata and decompresses the files to restore them to their original form.

### File/Folder Hiding Process
1. **Select a Main File**: The user selects the file where hidden files/folders will be stored.
2. **Hide a File**: The user selects a file to hide. It is encrypted and compressed, then added to the metadata.
3. **Hide a Folder**: The user selects a folder to hide. The folder is compressed, encrypted, and added to the metadata.
4. **Extract Files**: The user can select a folder to extract the hidden files, which will be decrypted and decompressed back to their original form.

---

## Usage

### Starting the Application
1. Run the script:
   ```
   python filenfile.py
   ```
2. The Tkinter-based graphical user interface (GUI) will open.

### Steps to Use:
1. **Select Source**: Click the "Select Source" button to choose the main file where hidden files will be stored.
2. **Merge File**: Click the "Merge File" button to hide a file in the selected main file.
3. **Compress Folder**: Click the "Compress Folder" button to hide an entire folder inside the main file.
4. **Extract**: Click the "Extract" button to retrieve all hidden files from the main file.

### File Selection:
- **Hide File**: Select a single file to hide. It will be compressed, encrypted, and stored inside the main file.
- **Hide Folder**: Select a folder to hide. The folder will be compressed into a `.tar.lzma` file, encrypted, and stored in the main file.
- **Extract**: Retrieve the files by selecting a directory where the files will be restored.

### Error Handling:
- The application will prompt you with error messages if required actions are not performed (such as selecting a main file or if there is no hidden data to extract).

---

## How to Modify or Extend
1. **Encryption Key**: The encryption key is stored in `filenfile/encryption_key.key`. You can modify the key generation and decryption logic if needed.
2. **Metadata Structure**: The metadata about hidden files is stored as a JSON object inside the file `filenfile/hidden_metadata.bin`. You can customize the metadata structure as necessary.
3. **Compression Algorithm**: The current compression algorithm used is LZMA. You can modify the `lzma` compression and decompression logic to use other methods.

---

## Security Considerations
- The encryption key is stored in `filenfile/encryption_key.key` and must be kept secure to maintain the confidentiality of the hidden files.
- If the encryption key is lost or deleted, it will not be possible to recover the hidden files.

---

## Troubleshooting
1. **No Hidden Files Found**: Ensure that you've hidden files/folders before attempting to extract them. If no files were hidden, metadata will be empty.
2. **Metadata or Key File Missing**: If either the metadata or encryption key file is deleted, the hidden files will be unrecoverable.
3. **File Not Being Compressed**: Ensure that the file you are trying to hide is not locked or in use by another program.

---

## License
This project is licensed under the MIT License.

---

## Credits
- This project uses the `cryptography` package for AES encryption.
- Tkinter is used for creating the GUI interface.

---

## Contributing
Feel free to fork the repository and submit pull requests for improvements, bug fixes, or additional features!
