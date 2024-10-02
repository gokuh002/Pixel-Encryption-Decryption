import tkinter as tk
from tkinter import filedialog, messagebox

def encrypt_image(path, key):
    try:
        print('Path of the image:', path)
        print('Encryption key:', key)

        with open(path, 'rb') as file:
            image_data = file.read()
        image_data = bytearray(image_data)

        for index, value in enumerate(image_data):
            image_data[index] = value ^ key

        with open(path, 'wb') as file:
            file.write(image_data)
        print('Encryption done...')
        messagebox.showinfo("Success", "Encrypted")

    except Exception as e:
        print('Error:', e)
        messagebox.showerror("Error", f'Error: {str(e)}')

def decrypt_image(path, key):
    try:
        print('Path of the image file:', path)
        print('Decryption key:', key)

        with open(path, 'rb') as file:
            image_data = file.read()
        image_data = bytearray(image_data)

        for index, value in enumerate(image_data):
            image_data[index] = value ^ key

        with open(path, 'wb') as file:
            file.write(image_data)
        print('Decryption done...')
        messagebox.showinfo("Success", "Decrypted")

    except Exception as e:
        print('Error:', e)
        messagebox.showerror("Error", f'Error: {str(e)}')

def browse_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        entry_path.delete(0, tk.END)
        entry_path.insert(0, file_path)

def process_image():
    image_path = entry_path.get()
    try:
        key = int(entry_key.get())
    except ValueError:
        messagebox.showerror("Invalid Key", "Please enter a valid integer for the key.")
        return
    operation = var_operation.get()
    if operation == 'encrypt':
        encrypt_image(image_path, key)
    elif operation == 'decrypt':
        decrypt_image(image_path, key)

# GUI
root = tk.Tk()
root.title("Image Encrypt/Decrypt")

tk.Label(root, text="Path:").grid(row=0, column=0, padx=10, pady=10)
entry_path = tk.Entry(root, width=50)
entry_path.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Key:").grid(row=1, column=0, padx=10, pady=10)
entry_key = tk.Entry(root, width=50)
entry_key.grid(row=1, column=1, padx=10, pady=10)

var_operation = tk.StringVar(value="encrypt")
tk.Radiobutton(root, text="Encrypt", variable=var_operation, value="encrypt").grid(row=2, column=0, padx=10, pady=10)
tk.Radiobutton(root, text="Decrypt", variable=var_operation, value="decrypt").grid(row=2, column=1, padx=10, pady=10)

tk.Button(root, text="Process", command=process_image).grid(row=3, columnspan=3, pady=20)

root.mainloop()
