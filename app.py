import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    length = int(length_entry.get())

    characters = ""
    if var_upper.get():
        characters += string.ascii_uppercase
    if var_lower.get():
        characters += string.ascii_lowercase
    if var_digits.get():
        characters += string.digits
    if var_special.get():
        characters += string.punctuation

    if not characters:
        messagebox.showwarning("Input Error", "Select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Length
tk.Label(root, text="Password Length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack()

# Options
var_upper = tk.BooleanVar()
var_lower = tk.BooleanVar()
var_digits = tk.BooleanVar()
var_special = tk.BooleanVar()

tk.Checkbutton(root, text="Include Uppercase Letters", variable=var_upper).pack(anchor='w')
tk.Checkbutton(root, text="Include Lowercase Letters", variable=var_lower).pack(anchor='w')
tk.Checkbutton(root, text="Include Numbers", variable=var_digits).pack(anchor='w')
tk.Checkbutton(root, text="Include Special Characters", variable=var_special).pack(anchor='w')

# Button
tk.Button(root, text="Generate Password", command=generate_password, bg="blue", fg="white").pack(pady=10)

# Result
tk.Label(root, text="Generated Password:", font=("Arial", 12)).pack()
result_entry = tk.Entry(root, font=("Arial", 12), width=30)
result_entry.pack()

root.mainloop()
