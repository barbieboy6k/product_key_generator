import tkinter as tk
from tkinter import messagebox
import hashlib
import string

def generate_product_key(email, password):
    def hash_input(input_string):
        return hashlib.sha3_256(input_string.encode()).hexdigest()
    
    def interleave_strings(s1, s2):
        max_len = max(len(s1), len(s2))
        s1 = s1.ljust(max_len, '0')
        s2 = s2.ljust(max_len, '0')
        return ''.join(a + b for a, b in zip(s1, s2))
    
    # Use a hash of the email as the salt to make the key generation deterministic
    salt = hashlib.sha3_256(email.encode()).hexdigest()
    email_hash = hash_input(email + salt)
    password_hash = hash_input(password + salt)
    interleaved_hash = interleave_strings(email_hash, password_hash)

    characters = string.ascii_uppercase + string.digits

    key_chars = [
        characters[int(interleaved_hash[i:i+2], 16) % len(characters)]
        for i in range(0, 50, 2)
    ]
    final_key = ''.join(key_chars[:25])
    formatted_key = '-'.join(final_key[i:i+5] for i in range(0, 25, 5))

    return formatted_key

def on_generate():
    email = email_entry.get()
    password = password_entry.get()
    if not email or not password:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return
    if "@" not in email or "." not in email:
        messagebox.showwarning("Invalid Email", "Please enter a valid email address!")
        return
    product_key = generate_product_key(email, password)
    result_label.config(text=f"Product Key: {product_key}")

def copy_to_clipboard(event):
    root.clipboard_clear()
    root.clipboard_append(result_label.cget("text").replace("Product Key: ", ""))
    messagebox.showinfo("Copied", "Product key copied to clipboard!")

# Create the main window
root = tk.Tk()
root.title("Product Key Generator")

# Set fixed size for the window
root.resizable(False, False)  # Disable resizing

# Create and place the widgets
email_label = tk.Label(root, text="Enter your email:")
email_label.grid(row=0, column=0, padx=10, pady=5)
email_entry = tk.Entry(root, width=30)
email_entry.grid(row=0, column=1, padx=10, pady=5)

password_label = tk.Label(root, text="Enter your password:")
password_label.grid(row=1, column=0, padx=10, pady=5)
password_entry = tk.Entry(root, show='*', width=30)
password_entry.grid(row=1, column=1, padx=10, pady=5)

generate_button = tk.Button(root, text="Generate Key", command=on_generate)
generate_button.grid(row=2, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="Product Key: ")
result_label.grid(row=3, column=0, columnspan=2, pady=10)
result_label.bind("<Button-1>", copy_to_clipboard)  # Bind left-click to copy function

# Run the application
root.mainloop()